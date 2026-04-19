import json

def load_events(file_path="events.jsonl"):
    events = []
    try:
        with open(file_path, "r") as f:
            for line in f:
                events.append(json.loads(line))
    except FileNotFoundError:
        return []
    return events
