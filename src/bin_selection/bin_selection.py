import numpy as np

def select_bin_from_chirp(chirp_fft_half_mag):
    peak_bin = np.argmax(chirp_fft_half_mag)
    return peak_bin

def select_bin_from_frame(frame_fft_half_mag):
    peak_bin = select_bin_from_chirp(frame_fft_half_mag[0]) # peak bin of 1st chirp
    return peak_bin