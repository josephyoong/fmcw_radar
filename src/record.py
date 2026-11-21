import argparse
from contextlib import closing
from datetime import datetime
from pathlib import Path

import numpy as np

import config as cfg
from sources import getSource

RECORDINGS_DIR = Path(__file__).resolve().parent.parent / "recordings"
PERIOD_RECORDING = 30


def save(frames, source, note):
    RECORDINGS_DIR.mkdir(exist_ok=True)
    path = RECORDINGS_DIR / f"{datetime.now():%Y%m%d-%H%M%S}-{source}.npz"
    # config travels with the frames, so an old recording stays interpretable
    np.savez(
        path,
        frames=np.array(frames), # [frames, chirps, samples]
        source=source,
        note=note,
        FREQ_MIN=cfg.FREQ_MIN,
        FREQ_MAX=cfg.FREQ_MAX,
        SAMPLE_RATE=cfg.SAMPLE_RATE,
        SAMPLES_PER_CHIRP=cfg.SAMPLES_PER_CHIRP,
        PERIOD_CHIRP_REPEAT=cfg.PERIOD_CHIRP_REPEAT,
        CHIRPS_PER_FRAME=cfg.CHIRPS_PER_FRAME,
        PERIOD_FRAME_REPEAT=cfg.PERIOD_FRAME_REPEAT,
    )
    print(f"saved {len(frames)} frames to {path}")
    return path


def record(numFrames, source="live", note=""):
    makeFrames = getSource(source)

    frames = []
    try:
        with closing(makeFrames(numFrames=numFrames)) as liveFrames:
            for frame in liveFrames:
                frames.append(frame)
                print(f"\rframe {len(frames)}/{numFrames}", end="", flush=True)
        print()
    finally:
        # keep whatever was captured, even on a sensor error or ctrl-c
        if frames:
            return save(frames, source, note)
        print("no frames captured")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="live")
    parser.add_argument("--frames", type=int,
                        default=round(PERIOD_RECORDING / cfg.PERIOD_FRAME_REPEAT))
    parser.add_argument("--note", default="", help="what the scene was")
    args = parser.parse_args()

    record(numFrames=args.frames, source=args.source, note=args.note)
