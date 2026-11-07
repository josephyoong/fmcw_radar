import time
import numpy as np

import config as cfg

PERIOD_RECORDING = 30
number_of_frames = round(PERIOD_RECORDING / cfg.PERIOD_FRAME_REPEAT)

def subject_range_model(t):
    TARGET_RANGE_M = 0.5
    BREATH_FREQ_HZ = 0.25
    BREATH_AMPL_M = 0.5e-3
    return TARGET_RANGE_M + BREATH_AMPL_M * np.sin(2 * np.pi * BREATH_FREQ_HZ * t)

def get_chirp(t_start):
    sample_times = np.arange(cfg.SAMPLES_PER_CHIRP) * cfg.period_sample
    subject_range = subject_range_model(t_start)
    freq_beat = 2 * subject_range * cfg.slope / cfg.c
    phase = 4 * np.pi * subject_range / cfg.wavelength
    return np.cos(2 * np.pi * freq_beat * sample_times + phase)

def get_frame(frame_index):
    t0 = frame_index * cfg.PERIOD_FRAME_REPEAT
    return np.array([get_chirp(t0 + i * cfg.PERIOD_CHIRP_REPEAT) for i in range(cfg.CHIRPS_PER_FRAME)])

def simulated_frames(n_frames=number_of_frames, realtime=True):
    for i in range(n_frames):
        if realtime:
            time.sleep(cfg.PERIOD_FRAME_REPEAT)
        frame = get_frame(i)
        yield frame