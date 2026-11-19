import numpy as np
import matplotlib.pyplot as plt

import config as cfg

plt.ion()

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

def plotRangeFFT(spectrum):
    plt.figure("range FFT")
    plt.cla()
    plt.plot(cfg.distance, np.abs(spectrum).mean(axis=0))
    plt.xlabel("range (m)")
    plt.ylabel("magnitude")
    plt.pause(0.001)
