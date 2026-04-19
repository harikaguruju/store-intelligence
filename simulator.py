import requests
import time
import random

API = "https://store-intelligence-j9m8.onrender.com"

while True:
    event = {
        "store_id": "STORE_001",
        "camera_id": random.choice(["CAM_1", "CAM_2", "CAM_3"]),
        "visitor_id": f"V{random.randint(1,10)}",
        "event_type": random.choices(
		["ENTRY", "EXIT"],
		weights=[0.7, 0.3]
	)[0]
    }

    try:
        requests.post(f"{API}/add-event", json=event)
        print("Event sent:", event)
    except:
        print("Server error")

    time.sleep(2)
