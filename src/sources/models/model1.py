import numpy as np
import time

import config as cfg

PERIOD_RECORDING = 30
NUM_FRAMES = round(PERIOD_RECORDING / cfg.PERIOD_FRAME_REPEAT)

def getDisplacement(times):
    return getRange(times) - getRange(times - cfg.PERIOD_CHIRP_REPEAT)

def getRange(time):
    r = 0.5
    # range scalar
    return r

def getChirp(startTime):
    sampleTimes = np.arange(cfg.SAMPLES_PER_CHIRP) * cfg.samplePeriod
    r = getRange(startTime) # assume constant range over chirp
    beatFreq = 2 * r * cfg.slope / cfg.c
    phase = 4 * np.pi * r / cfg.wavelength
    chirp = np.exp(1j * (2 * np.pi * beatFreq * sampleTimes + phase))
    # chirp array of samples; of length SAMPLES_PER_CHIRP
    return chirp

def getFrame(startTime):
    chirpStartTimes = startTime + (np.arange(cfg.CHIRPS_PER_FRAME) * cfg.PERIOD_CHIRP_REPEAT)
    chirps = []
    for chirpStartTime in chirpStartTimes:
        chirps.append(getChirp(chirpStartTime))
    frame = np.array(chirps)
    # frame array of chirps; of length CHIRPS_PER_FRAME
    return frame

def frameGenerator(numFrames=NUM_FRAMES, realtime=True):
    for i in range(numFrames):
        if realtime:
            time.sleep(cfg.PERIOD_FRAME_REPEAT)
        frameStartTime = i * cfg.PERIOD_FRAME_REPEAT
        frame = getFrame(frameStartTime)
        yield frame