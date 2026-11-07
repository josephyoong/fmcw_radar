def get_frames(source):
    if source == "model":
        from input.model import simulated_frames
        return simulated_frames()
    if source == "live":
        from input.live import live_frames
        return live_frames()
    raise ValueError(f"unknown source: {source}")