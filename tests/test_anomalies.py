from app.anomalies import detect_anomalies

def test_anomalies():
    events = [
        {"confidence": 0.9},
        {"confidence": 0.4},  # anomaly
        {"confidence": 0.8},
        {"confidence": 0.3}   # anomaly
    ]

    result = detect_anomalies(events)

    assert len(result) == 2
    assert result[0]["confidence"] == 0.4
    assert result[1]["confidence"] == 0.3
