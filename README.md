# UCCIS Signal Provider

## Overview

This project provides a deterministic Signal Provider designed to support operational runtime participation within the UCCIS integration chain.

The service exposes structured operational signals through FastAPI APIs and supports trace propagation, replay readiness, runtime evidence generation, and deterministic execution.

## Features

* Deterministic signal responses
* Stable signal identifiers
* Stable trace identifiers
* Trace propagation support
* Replay readiness
* Runtime evidence support
* Integration-ready operational datasets

## Runtime Chain

Signal

↓

Telemetry

↓

Incident

↓

Escalation

↓

Dashboard Visibility

↓

Replay Visibility

↓

Runtime Evidence

## API Endpoints

### GET /signals

Returns all operational signals.

### GET /signal/{signal_id}

Returns a specific signal.

### GET /telemetry

Returns telemetry information.

### GET /incident

Returns incident information.

### GET /escalation

Returns escalation information.

### GET /dashboard

Returns dashboard visibility information.

### GET /replay

Returns replay visibility information.

### GET /runtime-evidence

Returns runtime evidence information.

### GET /health

Returns service health information.

## Run Application

uvicorn app:app --reload

## Technologies Used

* Python
* FastAPI
* Uvicorn
* JSON Dataset Storage

## Status

Ready for deterministic runtime participation and UCCIS integration workflows.

