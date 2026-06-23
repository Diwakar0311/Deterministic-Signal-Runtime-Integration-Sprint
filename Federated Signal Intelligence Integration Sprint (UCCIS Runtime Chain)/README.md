# UCCIS Canonical Signal Layer

## Overview

The UCCIS Canonical Signal Layer serves as the official ingestion layer for the UCCIS Runtime Chain.

This implementation integrates signal generation directly into the canonical platform and supports downstream runtime participation.

## Supported Domains

- Traffic
- Water
- Flooding
- Weather
- Logistics
- Infrastructure
- Cargo
- Vessel Movement

## Runtime Chain

Signal

↓

Telemetry

↓

Incident

↓

Replay

## Features

- Canonical Signal Schema
- Deterministic Signal Records
- Trace Propagation
- Automatic Telemetry Generation
- Automatic Incident Creation
- Replay Reconstruction
- Load Test Validation

## API Endpoints

GET /signals

GET /signal/{signal_id}

GET /telemetry

GET /incident

GET /replay/{signal_id}

GET /health

## Run Application

```bash
uvicorn app:app --reload