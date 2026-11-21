import numpy as np

FREQ_MIN            = 59_133_931_281
FREQ_MAX            = 62_366_068_720
SAMPLE_RATE         = 1e6
SAMPLES_PER_CHIRP   = 64
PERIOD_CHIRP_REPEAT = 411.238e-6
CHIRPS_PER_FRAME    = 128
PERIOD_FRAME_REPEAT = 0.1

c               = 299_792_458.0
bandwidth       = FREQ_MAX - FREQ_MIN
samplePeriod    = 1 / SAMPLE_RATE
chirpPeriod     = samplePeriod * SAMPLES_PER_CHIRP
slope           = bandwidth / chirpPeriod
metersPerBin    = c / (2*bandwidth)
distance        = np.arange(SAMPLES_PER_CHIRP // 2) * metersPerBin
fc              = ((FREQ_MIN + FREQ_MAX) / 2)
wavelength      = c / fc
metresPerRad    = c / (4*np.pi*fc)
frameRate       = 1 / PERIOD_FRAME_REPEAT
hzPerMetre      = 2 * slope / c