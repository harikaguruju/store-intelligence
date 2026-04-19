import uuid
from ultralytics import YOLO
import cv2
from datetime import datetime
import json

# Load model
model = YOLO("yolov8n.pt")

# Videos list
videos = ["CAM 1.mp4", "CAM 2.mp4", "CAM 3.mp4", "CAM 4.mp4", "CAM 5.mp4"]

# Entry/Exit line position
line_y = 300

# Store tracking history
track_history = {}

# To avoid duplicate ENTRY/EXIT
counted_ids = set()

# 🔥 NEW: cooldown tracking
last_event_time = {}
cooldown_seconds = 3

# 🔥 ADD THIS (new)
person_state = {}

# 🔥 ADD THIS (NEW FIX)
entry_time = {}
min_stay_seconds = 3

# Open file to save events
file = open("events.jsonl", "w")

# LOOP THROUGH VIDEOS
for video_path in videos:

    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize for speed
        frame = cv2.resize(frame, (640, 480))

        # Tracking
        results = model.track(frame, persist=True, verbose=False)

        # Draw entry/exit line
        cv2.line(frame, (0, line_y), (640, line_y), (255, 0, 0), 2)

        for r in results:
            if r.boxes.id is not None:
                for box, track_id in zip(r.boxes, r.boxes.id):

                    if int(box.cls[0]) == 0:  # person
                        x1, y1, x2, y2 = map(int, box.xyxy[0])

                        # unique ID per video
                        track_id = f"{video_path}_{int(track_id)}"

                        # Draw box
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                        # Show ID
                        cv2.putText(frame, f"ID: {track_id}",
                                    (x1, y1 - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    0.6, (0, 255, 0), 2)

                        # Initialize history
                        if track_id not in track_history:
                            track_history[track_id] = []

                        # Store position
                        track_history[track_id].append((x1, y1))

                        # Keep last 2 points
                        if len(track_history[track_id]) > 2:
                            track_history[track_id].pop(0)

                        # Movement check
                        if len(track_history[track_id]) == 2:
                            y_prev = track_history[track_id][0][1]
                            y_curr = track_history[track_id][1][1]

                            current_time = datetime.now()

                            # Initialize state
                            if track_id not in person_state:
                                person_state[track_id] = "OUT"

                            # ENTRY
                            if y_prev < line_y and y_curr >= line_y:
                                if person_state[track_id] == "OUT":

                                    person_state[track_id] = "IN"

                                    # 🔥 ADD THIS
                                    entry_time[track_id] = current_time

                                    event = {
                                        "event_id": str(uuid.uuid4()),
					"store_id": "STORE_001",
                                        "camera_id": video_path,
                                        "visitor_id": track_id,
                                        "event_type": "ENTRY",
					"timestamp": current_time.isoformat(),
					"zone_id": None,
					"dwell_ms": 0,
					"is_staff": False,
					"confidence": 0.9,
					"metadata": {
						"queue_depth": None,
						"sku_zone": None,
						"session_seq": 0
					}
                                    }
                                    file.write(json.dumps(event) + "\n")
                                    file.flush()

                            # EXIT
                            if y_prev > line_y and y_curr <= line_y:
                                if person_state[track_id] == "IN":

                                    # 🔥 ADD THIS (filter fake exits)
                                    stay_time = 0
                                    if track_id in entry_time:
                                        stay_time = (current_time - entry_time[track_id]).seconds
                                        if stay_time < min_stay_seconds:
                                            continue

                                    person_state[track_id] = "OUT"

                                    event = {
                                        "event_id": str(uuid.uuid4()),
                                        "store_id": "STORE_001",
    					                          "camera_id": video_path,
    					                          "visitor_id": track_id,
    					                          "event_type": "EXIT",
    					                          "timestamp": current_time.isoformat(),
    					                          "zone_id": None,
    					                          "dwell_ms": stay_time * 1000,
    					                          "is_staff": False,
    					                          "confidence": 0.9,
    					                          "metadata": {
        					                        "queue_depth": None,
        					                        "sku_zone": None,
        					                        "session_seq": 0
    					                          }
				                              }
                                    file.write(json.dumps(event) + "\n")
                                    file.flush()

        # Show video
        cv2.imshow(video_path, frame)

        # ESC to stop ALL videos
        if cv2.waitKey(1) == 27:
            break

    cap.release()

file.close()
cv2.destroyAllWindows()
