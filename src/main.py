import numpy as np
import matplotlib.pyplot as plt
import time

import config as cfg
from input.model import simulated_frames
from range_fft.range_fft import frame_range_fft               

def main():
    # input data
    input_data = simulated_frames()

    # setup range FFT plot
    plt.ion()
    fig, ax = plt.subplots()
    bars = ax.bar(cfg.distance, np.zeros_like(cfg.distance), width=cfg.metres_per_bin * 0.8)
    ax.set_title("Range FFT)")
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Magnitude")
    half_bin = cfg.metres_per_bin / 2
    ax.set_xlim(cfg.distance[0] - half_bin, cfg.distance[-1] + half_bin)
    ax.set_ylim(0, 30)

    # per frame
    for frame in input_data:
        if not plt.fignum_exists(fig.number):
            break

        # range FFT
        frame_fft, frame_fft_half_mag = frame_range_fft(frame)

        # plot mean magnitude vs range
        frame_fft_mean_mag = frame_fft_half_mag.mean(axis=0)
        for bar, height in zip(bars, frame_fft_mean_mag):
            bar.set_height(height)
        plt.pause(0.001)

    plt.ioff()
    plt.show()
    
if __name__ == "__main__":
    main()