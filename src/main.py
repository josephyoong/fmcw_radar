from contextlib import closing
import numpy as np
import matplotlib.pyplot as plt
import argparse

import config as cfg
from sources import getSource, getTruth
from estimators import getEstimator
from evaluation.metrics import evaluate, report
import plots


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="model1")
    parser.add_argument("--estimator", default="estimator1")
    parser.add_argument("--plot", action="store_true")
    parser.add_argument("--plot-every", type=int, default=1, dest="plotEvery",
                        help="redraw every Nth frame; live plotting is slower than the frame rate")
    parser.add_argument("--evaluate", action="store_true")
    parser.add_argument("--frames", type=int, default=None)
    parser.add_argument("--snr-db", type=float, default=None, dest="snrDb")
    parser.add_argument("--recording", nargs="?", const="latest", default=None,
                        help="path to a .npz recording; bare flag uses the newest")
    parser.add_argument("--fast", action="store_true")
    return parser.parse_args()


def run(makeFrames, estimate, sourceArgs, plot=False, plotEvery=1):
    estimatedDisplacements = []
    timestamps = []

    with closing(makeFrames(**sourceArgs)) as frames:
        for frameIndex, frame in enumerate(frames):
            plotThisFrame = plot and frameIndex % plotEvery == 0

            # estimate
            estimatedDisplacement = estimate(frame, plot=plotThisFrame)

            chirpIndices = np.arange(1, estimatedDisplacement.size + 1)
            times = (frameIndex * cfg.PERIOD_FRAME_REPEAT + chirpIndices * cfg.PERIOD_CHIRP_REPEAT)

            estimatedDisplacements.append(estimatedDisplacement)
            timestamps.append(times)

            print(f"\rframe {frameIndex}", end="", flush=True)

            if plotThisFrame:
                allTimes = np.concatenate(timestamps)
                allDisplacements = np.concatenate(estimatedDisplacements)
                plots.plotDisplacement(allTimes, allDisplacements)
                plots.plotCumulativeDisplacement(allTimes, allDisplacements)

    return np.concatenate(timestamps), np.concatenate(estimatedDisplacements)


def main():
    args = parseArgs()

    # select source
    makeFrames = getSource(args.source)

    # select estimator
    estimate = getEstimator(args.estimator)

    sourceArgs = {"realtime": not args.fast}
    if args.frames is not None:
        sourceArgs["numFrames"] = args.frames
    if args.snrDb is not None:
            sourceArgs["snrDb"] = args.snrDb
    if args.recording is not None:
        sourceArgs["path"] = args.recording

    # estimate
    times, estimatedDisplacements = run(makeFrames, estimate, sourceArgs,
                                        plot=args.plot, plotEvery=args.plotEvery)

    # evaluate
    if args.evaluate:
        truthDisplacement = getTruth(args.source)
        report(evaluate(estimates=estimatedDisplacements, truth=truthDisplacement(times), plot=args.plot))

    plt.show(block=True)

if __name__ == "__main__":
    main()