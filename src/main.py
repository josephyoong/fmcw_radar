import numpy as np
import matplotlib.pyplot as plt
import argparse
from contextlib import closing

import config as cfg
from input import get_frames
from range_fft.range_fft import frame_range_fft    

def parse_args():
    parser = argparse.ArgumentParser(description="FMCW radar range FFT")
    parser.add_argument("--source", choices=("model", "live"), default="model", help="frame source: simulated model (default) or live radar")
    return parser.parse_args()

def main():
    args = parse_args()

    # setup range FFT plot
    plt.ion()
    fig, ax = plt.subplots()
    bars = ax.bar(cfg.distance, np.zeros_like(cfg.distance), width=cfg.metres_per_bin * 0.8)
    ax.set_title("Range FFT")
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Magnitude")
    half_bin = cfg.metres_per_bin / 2
    ax.set_xlim(cfg.distance[0] - half_bin, cfg.distance[-1] + half_bin)
    ax.set_ylim(0, 30)

    # get frames from chosen input source
    with closing(get_frames(args.source)) as input_data:

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