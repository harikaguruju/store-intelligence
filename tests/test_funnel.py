from app.funnel import compute_funnel

def test_funnel():
    events = [
        {"event_type": "ENTRY", "visitor_id": "1"},
        {"event_type": "ENTRY", "visitor_id": "2"},
        {"event_type": "EXIT", "visitor_id": "1"}
    ]

    result = compute_funnel(events)

    assert result["total_entered"] == 2
    assert result["total_exited"] == 1
    assert result["conversion_rate"] == 50.0
