from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

app = FastAPI(
    title="UCCIS Signal Provider",
    version="2.0"
)

with open("traffic.json", "r") as file:
    signals = json.load(file)


@app.get("/")
def root():
    return {
        "service": "UCCIS Signal Provider",
        "status": "running"
    }


@app.get("/signals")
def get_signals():
    return signals


@app.get("/signal/{signal_id}")
def get_signal(signal_id: str):

    for signal in signals:
        if signal["signal_id"] == signal_id:
            return signal

    return JSONResponse(
        status_code=404,
        content={
            "error": "SIGNAL_NOT_FOUND"
        }
    )


@app.get("/telemetry")
def telemetry():

    return {
        "telemetry_id": "TEL001",
        "trace_id": "TRACE_SIG001",
        "origin_signal_id": "SIG001",
        "status": "COLLECTED"
    }


@app.get("/incident")
def incident():

    return {
        "incident_id": "INC001",
        "trace_id": "TRACE_SIG001",
        "origin_signal_id": "SIG001",
        "status": "OPEN"
    }


@app.get("/escalation")
def escalation():

    return {
        "escalation_id": "ESC001",
        "trace_id": "TRACE_SIG001",
        "origin_signal_id": "SIG001",
        "status": "ESCALATED"
    }


@app.get("/dashboard")
def dashboard():

    return {
        "dashboard_visibility": True,
        "signals": len(signals),
        "status": "VISIBLE"
    }


@app.get("/replay")
def replay():

    return {
        "replay_visibility": True,
        "signal_id": "SIG001",
        "trace_id": "TRACE_SIG001"
    }


@app.get("/runtime-evidence")
def runtime_evidence():

    return {
        "signal_id": "SIG001",
        "telemetry_id": "TEL001",
        "incident_id": "INC001",
        "escalation_id": "ESC001",
        "runtime_evidence": "CAPTURED"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "signal-provider"
    }