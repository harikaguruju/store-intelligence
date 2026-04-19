def compute_funnel(events):
    entries = set()
    exits = set()

    for event in events:
        if event["event_type"] == "ENTRY":
            entries.add(event["visitor_id"])
        elif event["event_type"] == "EXIT":
            exits.add(event["visitor_id"])

    total_entered = len(entries)
    total_exited = len(exits)

    conversion_rate = 0
    if total_entered > 0:
        conversion_rate = ((total_entered - total_exited) / total_entered) * 100

    return {
        "total_entered": total_entered,
        "total_exited": total_exited,
        "conversion_rate": round(conversion_rate, 2)
    }
