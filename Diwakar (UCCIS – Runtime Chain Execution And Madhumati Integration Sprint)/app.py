from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import json
import os
import time

from trace import (
    generate_trace_id,
    generate_telemetry_id,
    generate_incident_id,
    generate_escalation_id
)

app = FastAPI(
    title="UCCIS Runtime Chain Engine",
    version="3.0"
)

SIGNALS_FILE = "traffic.json"
TELEMETRY_FILE = "telemetry.json"
INCIDENT_FILE = "incidents.json"
ESCALATION_FILE = "escalations.json"
REPLAY_FILE = "replay_sessions.json"
RUNTIME_LOG_FILE = "runtime_logs.json"


class ExecuteSignalRequest(BaseModel):
    signal_id: str


def load_json(file_name):

    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            json.dump([], f)

    with open(file_name, "r") as f:
        return json.load(f)


def save_json(file_name, data):

    with open(file_name, "w") as f:
        json.dump(data, f, indent=2)


@app.get("/")
def root():

    return {
        "service": "UCCIS Runtime Chain Engine",
        "status": "RUNNING"
    }


@app.get("/signals")
def get_signals():

    return load_json(SIGNALS_FILE)


@app.get("/signal/{signal_id}")
def get_signal(signal_id: str):

    signals = load_json(SIGNALS_FILE)

    for signal in signals:

        if signal["signal_id"] == signal_id:
            return signal

    raise HTTPException(
        status_code=404,
        detail="SIGNAL_NOT_FOUND"
    )

@app.post("/execute-signal")
def execute_signal(payload: ExecuteSignalRequest):

    start_time = time.time()

    signals = load_json(SIGNALS_FILE)

    signal = None

    for item in signals:

        if item["signal_id"] == payload.signal_id:
            signal = item
            break

    if signal is None:

        raise HTTPException(
            status_code=404,
            detail="SIGNAL_NOT_FOUND"
        )

    trace_id = signal["trace_id"]

    telemetry_records = load_json(
        TELEMETRY_FILE
    )

    incident_records = load_json(
        INCIDENT_FILE
    )

    escalation_records = load_json(
        ESCALATION_FILE
    )

    replay_records = load_json(
        REPLAY_FILE
    )

    runtime_logs = load_json(
        RUNTIME_LOG_FILE
    )

    timestamp = datetime.utcnow().isoformat()

    telemetry_id = generate_telemetry_id()

    telemetry = {
        "telemetry_id": telemetry_id,
        "trace_id": trace_id,
        "signal_id": signal["signal_id"],
        "payload": {
            "source": "UCCIS Runtime"
        },
        "origin_signal_id": signal["signal_id"],
        "parent_reference": signal["signal_id"],
        "created_at": timestamp,
        "status": "COLLECTED"
    }

    telemetry_records.append(telemetry)

    incident_id = generate_incident_id()

    incident = {
        "incident_id": incident_id,
        "trace_id": trace_id,
        "telemetry_id": telemetry_id,
        "origin_signal_id": signal["signal_id"],
        "parent_reference": telemetry_id,
        "severity": "HIGH",
        "status": "OPEN",
        "created_at": timestamp
    }

    incident_records.append(incident)

    escalation_id = generate_escalation_id()

    escalation = {
        "escalation_id": escalation_id,
        "trace_id": trace_id,
        "incident_id": incident_id,
        "origin_signal_id": signal["signal_id"],
        "parent_reference": incident_id,
        "level": "LEVEL-1",
        "status": "ACTIVE",
        "created_at": timestamp
    }

    escalation_records.append(escalation)

    replay_record = {
        "trace_id": trace_id,
        "signal": signal,
        "telemetry": telemetry,
        "incident": incident,
        "escalation": escalation,
        "timeline": [
            {
                "step": 1,
                "event": "Signal Created",
                "reference": signal["signal_id"]
            },
            {
                "step": 2,
                "event": "Telemetry Created",
                "reference": telemetry_id
            },
            {
                "step": 3,
                "event": "Incident Created",
                "reference": incident_id
            },
            {
                "step": 4,
                "event": "Escalation Created",
                "reference": escalation_id
            }
        ]
    }

    replay_records.append(replay_record)

    execution_duration = round(
        (time.time() - start_time) * 1000,
        2
    )

    runtime_log = {
        "trace_id": trace_id,
        "execution_timestamp": timestamp,
        "execution_duration_ms": execution_duration,
        "generated_ids": {
            "signal_id": signal["signal_id"],
            "telemetry_id": telemetry_id,
            "incident_id": incident_id,
            "escalation_id": escalation_id
        },
        "runtime_events": [
            "Signal Created",
            "Telemetry Created",
            "Incident Created",
            "Escalation Created"
        ]
    }

    runtime_logs.append(runtime_log)

    save_json(
        TELEMETRY_FILE,
        telemetry_records
    )

    save_json(
        INCIDENT_FILE,
        incident_records
    )

    save_json(
        ESCALATION_FILE,
        escalation_records
    )

    save_json(
        REPLAY_FILE,
        replay_records
    )

    save_json(
        RUNTIME_LOG_FILE,
        runtime_logs
    )

    return {
        "trace_id": trace_id,
        "signal_id": signal["signal_id"],
        "telemetry_id": telemetry_id,
        "incident_id": incident_id,
        "escalation_id": escalation_id,
        "execution_duration_ms": execution_duration
    }


@app.get("/telemetry")
def telemetry():

    return load_json(
        TELEMETRY_FILE
    )


@app.get("/incident")
def incident():

    return load_json(
        INCIDENT_FILE
    )


@app.get("/escalation")
def escalation():

    return load_json(
        ESCALATION_FILE
    )


@app.get("/replay/{trace_id}")
def replay(trace_id: str):

    replay_records = load_json(
        REPLAY_FILE
    )

    for replay in replay_records:

        if replay["trace_id"] == trace_id:
            return replay

    raise HTTPException(
        status_code=404,
        detail="TRACE_NOT_FOUND"
    )


@app.get("/runtime-evidence")
def runtime_evidence():

    return load_json(
        RUNTIME_LOG_FILE
    )
@app.get("/dashboard")
def dashboard():

    signals = load_json(
        SIGNALS_FILE
    )

    telemetry = load_json(
        TELEMETRY_FILE
    )

    incidents = load_json(
        INCIDENT_FILE
    )

    escalations = load_json(
        ESCALATION_FILE
    )

    replay_sessions = load_json(
        REPLAY_FILE
    )

    runtime_logs = load_json(
        RUNTIME_LOG_FILE
    )

    active_signals = len(signals)

    active_incidents = len(
        incidents
    )

    active_escalations = len(
        escalations
    )

    recent_executions = len(
        runtime_logs
    )

    replay_count = len(
        replay_sessions
    )

    runtime_health = "HEALTHY"

    if (
        active_signals == 0 and
        len(telemetry) == 0
    ):
        runtime_health = "NO_DATA"

    if active_incidents > 10:
        runtime_health = "WARNING"

    if active_incidents > 20:
        runtime_health = "CRITICAL"

    return {
        "active_signals": active_signals,
        "active_incidents": active_incidents,
        "active_escalations": active_escalations,
        "recent_executions": recent_executions,
        "replay_count": replay_count,
        "runtime_health": runtime_health
    }


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "signal-provider"
    }