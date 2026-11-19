import numpy as np

import config as cfg

def displacementVariance(snrDb, numSamples=cfg.SAMPLES_PER_CHIRP, metresPerRad=cfg.metresPerRad):
    snr = 10 ** (np.asarray(snrDb, dtype=float) / 10)
    crlb = metresPerRad**2 / (numSamples * snr)
    return crlb