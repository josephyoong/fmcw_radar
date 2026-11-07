import numpy as np

FREQ_MIN            = 59_133_931_281
FREQ_MAX            = 62_366_068_720
SAMPLE_RATE         = 1e6
SAMPLES_PER_CHIRP   = 64
PERIOD_CHIRP_REPEAT = 411.238e-6
CHIRPS_PER_FRAME    = 64
PERIOD_FRAME_REPEAT = 0.1

c               = 3e8
bandwidth       = FREQ_MAX - FREQ_MIN
period_sample   = 1 / SAMPLE_RATE
period_chirp    = period_sample * SAMPLES_PER_CHIRP
slope           = bandwidth / period_chirp
metres_per_bin  = c / (2*bandwidth)
distance        = np.arange(SAMPLES_PER_CHIRP // 2) * metres_per_bin
wavelength      = c / ((FREQ_MIN + FREQ_MAX) / 2)
metres_per_rad  = wavelength / (4*np.pi)
frame_rate      = 1 / PERIOD_FRAME_REPEAT