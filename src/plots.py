import numpy as np
import matplotlib.pyplot as plt

import config as cfg

WINDOW_SECONDS = 5.0

plt.ion()
plt.rcParams["figure.raise_window"] = False

def plotSweep(snrsDb, mses, crlb):
    plt.figure("variance vs SNR")
    plt.cla()
    plt.semilogy(snrsDb, mses, "o-", label="measured")
    plt.semilogy(snrsDb, crlb, "--", label="CRLB")
    plt.xlabel("SNR (dB)")
    plt.ylabel("MSE (m^2)")
    plt.legend()
    plt.pause(0.001)

def plotError(error):
    plt.figure("error")
    plt.cla()
    plt.hist(error, bins=50)
    plt.xlabel("error (m)")
    plt.ylabel("count")
    plt.pause(0.001)

def plotRangeFFT(spectrum, peakBin=None):
    plt.figure("range FFT")
    plt.cla()
    magnitude = np.abs(spectrum).mean(axis=0)
    plt.plot(cfg.distance, magnitude)
    if peakBin is not None:
        plt.plot(cfg.distance[peakBin], magnitude[peakBin], "rx", markersize=10,
                 label=f"selected bin {peakBin} ({cfg.distance[peakBin]:.3f} m)")
        plt.legend()
    plt.xlabel("range (m)")
    plt.ylabel("magnitude")
    plt.pause(0.001)

def plotBinVariation(squaredDeviation):
    plt.figure("bin variation")
    plt.cla()
    plt.plot(cfg.distance, squaredDeviation.mean(axis=0))
    plt.xlabel("range (m)")
    plt.ylabel("mean squared deviation")
    plt.pause(0.001)

def plotCumulativeDisplacement(times, displacements):
    plt.figure("cumulative displacement vs time")
    plt.cla()
    plt.plot(times, np.cumsum(displacements))
    plt.xlabel("time (s)")
    plt.ylabel("cumulative displacement (m)")
    plt.pause(0.001)

def plotDisplacement(times, displacements):
    plt.figure("displacement vs time")
    plt.cla()
    timeEnd = max(times[-1], WINDOW_SECONDS)
    timeStart = timeEnd - WINDOW_SECONDS
    window = times >= timeStart
    plt.plot(times[window], displacements[window], ".", markersize=2)
    plt.xlim(timeStart, timeEnd)
    plt.xlabel("time (s)")
    plt.ylabel("displacement (m)")
    plt.pause(0.001)
