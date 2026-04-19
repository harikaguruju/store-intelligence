from app.metrics import compute_metrics

def test_metrics():
    events = [
        {"event_type": "ENTRY"},
        {"event_type": "ENTRY"},
        {"event_type": "EXIT"}
    ]

    result = compute_metrics(events)

    assert result["total_entries"] == 2
    assert result["total_exits"] == 1
    assert result["current_inside"] == 1
