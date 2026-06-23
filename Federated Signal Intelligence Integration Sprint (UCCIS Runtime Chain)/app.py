from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

from telemetry import generate_telemetry
from incident import generate_incident
from replay import reconstruct

app = FastAPI(
    title="UCCIS Canonical Signal Layer",
    version="3.0"
)

with open("traffic.json", "r") as file:
    signals = json.load(file)


@app.get("/")
def root():
    return {
        "service": "UCCIS Canonical Signal Layer",
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

    telemetry_records = []

    for signal in signals:
        telemetry_records.append(
            generate_telemetry(signal)
        )

    return telemetry_records


@app.get("/incident")
def incident():

    incident_records = []

    for signal in signals:
        incident_records.append(
            generate_incident(signal)
        )

    return incident_records


@app.get("/replay/{signal_id}")
def replay(signal_id: str):

    for signal in signals:

        if signal["signal_id"] == signal_id:

            telemetry = generate_telemetry(signal)

            incident = generate_incident(signal)

            return reconstruct(
                signal,
                telemetry,
                incident
            )

    return JSONResponse(
        status_code=404,
        content={
            "error": "SIGNAL_NOT_FOUND"
        }
    )


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "uccis-canonical-signal-layer"
    }