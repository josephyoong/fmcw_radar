import numpy as np

import config as cfg
import plots

# frame array of M chirps
# option to set plotting on vs off?
def estimateDisplacement(frame, plot=False):
    spectrum = np.fft.fft(frame, axis=-1)
    spectrum = spectrum[:, :cfg.SAMPLES_PER_CHIRP // 2]

    if plot:
        plots.plotRangeFFT(spectrum)

    # peakBin = np.argmax(np.abs(spectrum[0]))
    # phases = np.angle(spectrum[:, peakBin])
    # displacement = np.diff(phases) * cfg.metresPerRad
    # i dont get this change
    peakBin = np.argmax(np.abs(spectrum).mean(axis=0))
    peak = spectrum[:, peakBin]
    displacement = np.angle(peak[1:] * np.conj(peak[:-1])) * cfg.metresPerRad
    # displacement array of length M
    return displacement