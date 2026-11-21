import numpy as np

import config as cfg
import plots

# frame array of M chirps
def estimateDisplacement(frame, plot=False):
    spectrum = np.fft.fft(frame, axis=-1)
    spectrum = spectrum[:, :cfg.SAMPLES_PER_CHIRP // 2]

    # per bin, over the chirps of this frame
    binMean = spectrum.mean(axis=0)
    deviation = spectrum - binMean
    squaredDeviation = np.abs(deviation) ** 2

    # select the bin that varies most over the frame, not the strongest one
    peakBin = np.argmax(squaredDeviation.mean(axis=0))

    if plot:
        plots.plotRangeFFT(spectrum, peakBin=peakBin)
        plots.plotBinVariation(squaredDeviation)


    peak = spectrum[:, peakBin]
    displacement = np.angle(peak[1:] * np.conj(peak[:-1])) * cfg.metresPerRad
    # displacement array of length M
    return displacement
