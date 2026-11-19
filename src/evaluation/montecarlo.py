import numpy as np

import config as cfg
import plots
from main import run
from sources import getSource
from estimators import getEstimator
from evaluation.metrics import evaluate
from evaluation.crlb import displacementVariance

SNRS_DB = np.arange(-40, 50, 5)
NUM_FRAMES = 1000


def sweep(source="model2", estimator="estimator1", numFrames=NUM_FRAMES):
    makeFrames = getSource(source)
    estimate = getEstimator(estimator)

    mses = []
    crlbs = []

    print(f"{'SNR (dB)':>9} {'MSE (m2)':>12} {'CRLB (m2)':>12} {'MSE/CRLB':>9}")
    for snrDb in SNRS_DB:
        sourceArgs = {"realtime": False, "numFrames": numFrames, "snrDb": snrDb}
        estimates = run(makeFrames, estimate, sourceArgs)
        results = evaluate(estimates=estimates, truth=0.0, plot=False)
        crlb = displacementVariance(snrDb)
        mses.append(results["mse"])
        crlbs.append(crlb)
        print(f"{snrDb:>9.1f} {results['mse']:>12.4e} {crlb:>12.4e} "
              f"{results['mse'] / crlb:>9.2f}")

    return np.array(mses), np.array(crlbs)


if __name__ == "__main__":
    import argparse
    import matplotlib.pyplot as plt

    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="model2")
    parser.add_argument("--estimator", default="estimator1")
    parser.add_argument("--frames", type=int, default=NUM_FRAMES)
    args = parser.parse_args()

    mses, crlb = sweep(source=args.source, estimator=args.estimator, numFrames=args.frames)
    plots.plotSweep(SNRS_DB, mses, crlb)
    plt.show(block=True)