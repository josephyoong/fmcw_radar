import time
from pathlib import Path

import numpy as np

import config as cfg

RECORDINGS_DIR = Path(__file__).resolve().parent.parent.parent / "recordings"


def getPath(path="latest"):
    if path == "latest":
        recordings = sorted(RECORDINGS_DIR.glob("*.npz"))
        if not recordings:
            raise FileNotFoundError(f"no recordings in {RECORDINGS_DIR}")
        return recordings[-1]
    return Path(path)


def checkConfig(data):
    # the estimators slice by the current config, so a mismatch misreads the frames
    for name in ("SAMPLES_PER_CHIRP", "CHIRPS_PER_FRAME", "PERIOD_CHIRP_REPEAT",
                 "PERIOD_FRAME_REPEAT", "FREQ_MIN", "FREQ_MAX", "SAMPLE_RATE"):
        if name not in data:
            continue
        recorded = data[name].item()
        current = getattr(cfg, name)
        if recorded != current:
            print(f"warning: {name} was {recorded} when recorded, config.py now says {current}")


def frameGenerator(path="latest", numFrames=None, realtime=True):
    path = getPath(path)
    data = np.load(path)
    checkConfig(data)

    frames = data["frames"] # [frames, chirps, samples]
    note = str(data["note"]) if "note" in data else ""
    print(f"replaying {path.name}: {len(frames)} frames{f' ({note})' if note else ''}")

    if numFrames is not None:
        frames = frames[:numFrames]

    for frame in frames:
        if realtime:
            time.sleep(cfg.PERIOD_FRAME_REPEAT)
        yield frame
