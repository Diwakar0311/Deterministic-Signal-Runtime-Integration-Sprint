from datetime import datetime

def generate_telemetry(signal):

    return {
        "telemetry_id": f"TEL_{signal['signal_id']}",
        "trace_id": signal["trace_id"],
        "origin_signal_id": signal["signal_id"],
        "collected_at": datetime.utcnow().isoformat(),
        "status": "COLLECTED"
    }