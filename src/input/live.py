import numpy as np

import config as cfg

RX_ANTENNA     = 0
TX_POWER_LEVEL = 31
IF_GAIN_DB     = 33
LP_CUTOFF_HZ   = 500_000
HP_CUTOFF_HZ   = 80_000

def build_sequence_config():
    from ifxradarsdk.fmcw.types import FmcwSequenceChirp, FmcwSimpleSequenceConfig

    return FmcwSimpleSequenceConfig(
        frame_repetition_time_s=cfg.PERIOD_FRAME_REPEAT,
        chirp_repetition_time_s=cfg.PERIOD_CHIRP_REPEAT,
        num_chirps=cfg.CHIRPS_PER_FRAME,
        tdm_mimo=False,
        chirp=FmcwSequenceChirp(
            start_frequency_Hz=cfg.FREQ_MIN,
            end_frequency_Hz=cfg.FREQ_MAX,
            sample_rate_Hz=cfg.SAMPLE_RATE,
            num_samples=cfg.SAMPLES_PER_CHIRP,
            rx_mask=1 << RX_ANTENNA,
            tx_mask=1,
            tx_power_level=TX_POWER_LEVEL,
            lp_cutoff_Hz=LP_CUTOFF_HZ,
            hp_cutoff_Hz=HP_CUTOFF_HZ,
            if_gain_dB=IF_GAIN_DB,
        ),
    )

def live_frames(n_frames=0):
    from ifxradarsdk import get_version_full
    from ifxradarsdk.fmcw import DeviceFmcw

    with DeviceFmcw() as device:
        print("Radar SDK:", get_version_full())
        print("Sensor:   ", device.get_sensor_type())

        sequence = device.create_simple_sequence(build_sequence_config())
        device.set_acquisition_sequence(sequence)

        count = 0
        while n_frames == 0 or count < n_frames:
            frame = device.get_next_frame()[0] # [rx, chirps, samples]
            yield np.asarray(frame[0], dtype=float)
            count += 1
