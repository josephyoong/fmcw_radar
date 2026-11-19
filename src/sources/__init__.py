def getSource(source):
    if source == "live":
        from sources.live import liveFrames
        return liveFrames
    if source == "model1":
            from sources.models.model1 import frameGenerator
            return frameGenerator
    if source == "model2":
            from sources.models.model2 import frameGenerator
            return frameGenerator
    raise ValueError(f"unknown source: {source}")