from contextlib import closing
import numpy as np
import matplotlib.pyplot as plt
import argparse

from sources import getSource
from estimators import getEstimator
from evaluation.metrics import evaluate, report


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="model1")
    parser.add_argument("--estimator", default="estimator1")
    parser.add_argument("--plot", action="store_true")
    parser.add_argument("--evaluate", action="store_true")
    parser.add_argument("--frames", type=int, default=None)
    parser.add_argument("--snr-db", type=float, default=None, dest="snrDb")
    parser.add_argument("--fast", action="store_true")
    return parser.parse_args()


def run(makeFrames, estimate, sourceArgs, plot=False):
    estimatedDisplacements = []

    with closing(makeFrames(**sourceArgs)) as frames:
        for frame in frames:
            # estimate
            estimatedDisplacement = estimate(frame, plot=plot)

            estimatedDisplacements.append(estimatedDisplacement)

    return np.concatenate(estimatedDisplacements)


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

    estimatedDisplacements = run(makeFrames, estimate, sourceArgs, plot=args.plot)

    # evaluate
    if args.evaluate:
        report(evaluate(estimates=estimatedDisplacements, truth=0.0, plot=args.plot))

    plt.show(block=True)

if __name__ == "__main__":
    main()