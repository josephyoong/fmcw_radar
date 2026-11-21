import numpy as np

import plots

def report(results):
    print(f"{'n':>9} {results['n']}")
    for key in ("mean", "bias", "variance", "mse", "rmse"):
        print(f"{key:>9} {results[key]:>12.4e}")

def evaluate(estimates, truth, plot=True):
    error = estimates - truth

    results = {
        "n":        estimates.size,
        "mean":     estimates.mean(),
        "bias":     error.mean(),
        "variance": error.var(),
        "mse":      (error**2).mean(),
        "rmse":     np.sqrt((error**2).mean()),
    }

    if plot:
        plots.plotError(error)

    return results