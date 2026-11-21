import numpy as np
import time

import config as cfg

PERIOD_RECORDING = 30
NUM_FRAMES = round(PERIOD_RECORDING / cfg.PERIOD_FRAME_REPEAT)

RANGE_MEAN = 0.5 # 0.510145 for ~exactly on bin
DISPLACEMENT_AMPLITUDE = 3e-3
FREQ_OSCILLATION = 0.3

AMPLITUDE = 1.0
SNR_DB = 3.0
rng = np.random.default_rng(0)

# stationary clutter: single point, stronger than the oscillating target
CLUTTER_RANGE = 1.0 # 1.020290 for ~exactly on bin
CLUTTER_AMPLITUDE = 5.0

def noiseVariance(snrDb, amplitude=AMPLITUDE):
    signalPower = amplitude**2
    return signalPower / 10**(snrDb / 10)

def getDisplacement(times):
    return getRange(times) - getRange(times - cfg.PERIOD_CHIRP_REPEAT)

def getRange(time):
    r = RANGE_MEAN + DISPLACEMENT_AMPLITUDE * np.sin(2 * np.pi * FREQ_OSCILLATION * time)
    # range scalar
    return r

def getReflection(r, amplitude, sampleTimes):
    beatFreq = 2 * r * cfg.slope / cfg.c
    phase = 4 * np.pi * r / cfg.wavelength
    # reflection array of samples; of length SAMPLES_PER_CHIRP
    return amplitude * np.exp(1j * (2 * np.pi * beatFreq * sampleTimes + phase))

def getChirp(startTime, snrDb):
    sampleTimes = np.arange(cfg.SAMPLES_PER_CHIRP) * cfg.samplePeriod
    r = getRange(startTime) # assume constant range over chirp
    target = getReflection(r, AMPLITUDE, sampleTimes)
    clutter = getReflection(CLUTTER_RANGE, CLUTTER_AMPLITUDE, sampleTimes)
    sigma = np.sqrt(noiseVariance(snrDb) / 2) # SNR is against the target, not the clutter
    noise = rng.normal(0, sigma, cfg.SAMPLES_PER_CHIRP) + 1j * rng.normal(0, sigma, cfg.SAMPLES_PER_CHIRP)
    # chirp array of samples; of length SAMPLES_PER_CHIRP
    return target + clutter + noise

def getFrame(startTime, snrDb):
    chirpStartTimes = startTime + (np.arange(cfg.CHIRPS_PER_FRAME) * cfg.PERIOD_CHIRP_REPEAT)
    chirps = []
    for chirpStartTime in chirpStartTimes:
        chirps.append(getChirp(chirpStartTime, snrDb))
    frame = np.array(chirps)
    # frame array of chirps; of length CHIRPS_PER_FRAME
    return frame

def frameGenerator(numFrames=NUM_FRAMES, realtime=True, snrDb = SNR_DB):
    for i in range(numFrames):
        if realtime:
            time.sleep(cfg.PERIOD_FRAME_REPEAT)
        frameStartTime = i * cfg.PERIOD_FRAME_REPEAT
        frame = getFrame(frameStartTime, snrDb)
        # frame array of chirps; of length CHIRPS_PER_FRAME
        yield frame
