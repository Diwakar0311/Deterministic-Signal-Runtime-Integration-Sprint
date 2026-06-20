# Madhumati Integration Map

## Objective

Map Signal Provider runtime outputs to Madhumati UCCIS runtime inputs.

---

## What UCCIS Generates

Signal

Telemetry

Incident

Escalation

Replay Session

Runtime Evidence

Runtime Logs

---

## What Madhumati Consumes

### Signal Layer

signal_id

trace_id

signal_type

status

created_at

### Telemetry Layer

telemetry_id

trace_id

signal_id

payload

created_at

### Incident Layer

incident_id

trace_id

telemetry_id

severity

status

created_at

### Escalation Layer

escalation_id

trace_id

incident_id

level

status

created_at

### Dashboard Layer

signals

telemetry

incidents

escalations

replay_sessions

runtime_logs

trace_ids

---

## Current Gaps

Replay storage format alignment

Shared schema evolution

Common runtime contracts

---

## Required Contracts

Common trace_id propagation

Signal → Telemetry

Telemetry → Incident

Incident → Escalation

Replay reconstruction compatibility

Dashboard visibility compatibility

---

## Future Merge Plan

Adopt common runtime schema.

Adopt common replay structure.

Adopt common dashboard metrics.

Enable runtime chain convergence.