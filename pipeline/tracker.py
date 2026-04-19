def update_tracking(track_history, track_id, x, y):
    if track_id not in track_history:
        track_history[track_id] = []

    track_history[track_id].append((x, y))

    if len(track_history[track_id]) > 2:
        track_history[track_id].pop(0)

    return track_history[track_id]
