import uuid

def generate_trace_id():
    return f"TRACE_{uuid.uuid4().hex[:8]}"

def generate_telemetry_id():
    return f"TEL_{uuid.uuid4().hex[:8]}"

def generate_incident_id():
    return f"INC_{uuid.uuid4().hex[:8]}"

def generate_escalation_id():
    return f"ESC_{uuid.uuid4().hex[:8]}"