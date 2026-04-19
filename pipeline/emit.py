import uuid
from datetime import datetime

def create_event(event_type, visitor_id, camera_id, dwell_ms=0):
    return {
        "event_id": str(uuid.uuid4()),
        "store_id": "STORE_001",
        "camera_id": camera_id,
        "visitor_id": visitor_id,
        "event_type": event_type,
        "timestamp": datetime.now().isoformat(),
        "zone_id": None,
        "dwell_ms": dwell_ms,
        "is_staff": False,
        "confidence": 0.9,
        "metadata": {
            "queue_depth": None,
            "sku_zone": None,
            "session_seq": 0
        }
    }
