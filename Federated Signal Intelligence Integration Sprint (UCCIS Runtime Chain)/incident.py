from datetime import datetime

def generate_incident(signal):

    return {
        "incident_id": f"INC_{signal['signal_id']}",
        "trace_id": signal["trace_id"],
        "origin_signal_id": signal["signal_id"],
        "severity": signal["status"],
        "created_at": datetime.utcnow().isoformat(),
        "status": "OPEN"
    }