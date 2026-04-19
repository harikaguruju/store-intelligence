def detect_anomalies(events):
    anomalies = []

    for event in events:
        if event["confidence"] < 0.5:
            anomalies.append(event)

    return anomalies
