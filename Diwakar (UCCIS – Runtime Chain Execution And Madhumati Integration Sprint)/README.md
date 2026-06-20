# UCCIS Runtime Chain Engine

## Overview

Runtime execution engine for UCCIS operational chain.

## Runtime Chain

Signal

↓

Telemetry

↓

Incident

↓

Escalation

↓

Replay

↓

Runtime Evidence

↓

Dashboard

## Features

Runtime execution

Runtime persistence

Trace propagation

Replay reconstruction

Runtime evidence generation

Dashboard runtime participation

## Endpoints

GET /signals

GET /signal/{signal_id}

POST /execute-signal

GET /telemetry

GET /incident

GET /escalation

GET /replay/{trace_id}

GET /runtime-evidence

GET /dashboard

GET /health

## Run

uvicorn app:app --reload