def compute_metrics(events):
    total_entries = 0
    total_exits = 0

    for event in events:
        if event["event_type"] == "ENTRY":
            total_entries += 1
        elif event["event_type"] == "EXIT":
            total_exits += 1

    return {
        "total_entries": total_entries,
        "total_exits": total_exits,
        "current_inside": total_entries - total_exits
    }
