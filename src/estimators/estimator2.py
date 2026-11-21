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

    if plot:
        plots.plotRangeFFT(spectrum)
        plots.plotBinVariation(squaredDeviation)

    # bin selection unchanged for now
    peakBin = np.argmax(np.abs(spectrum).mean(axis=0))
    peak = spectrum[:, peakBin]
    displacement = np.angle(peak[1:] * np.conj(peak[:-1])) * cfg.metresPerRad
    # displacement array of length M
    return displacement
