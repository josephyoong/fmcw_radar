def getSource(source):
    if source == "live":
        from sources.live import liveFrames
        return liveFrames
    if source == "recording":
        from sources.recording import frameGenerator
        return frameGenerator
    if source == "model1":
            from sources.models.model1 import frameGenerator
            return frameGenerator
    if source == "model2":
            from sources.models.model2 import frameGenerator
            return frameGenerator
    if source == "model3":
                from sources.models.model3 import frameGenerator
                return frameGenerator
    if source == "model4":
        from sources.models.model4 import frameGenerator
        return frameGenerator
    if source == "model5":
        from sources.models.model5 import frameGenerator
        return frameGenerator
    raise ValueError(f"unknown source: {source}")

def getTruth(source):
    if source == "model1":
        from sources.models.model1 import getDisplacement
        return getDisplacement
    if source == "model2":
        from sources.models.model2 import getDisplacement
        return getDisplacement
    if source == "model3":
        from sources.models.model3 import getDisplacement
        return getDisplacement
    if source == "model4":
        from sources.models.model4 import getDisplacement
        return getDisplacement
    if source == "model5":
        from sources.models.model5 import getDisplacement
        return getDisplacement
    raise ValueError(f"no truth for source: {source}")