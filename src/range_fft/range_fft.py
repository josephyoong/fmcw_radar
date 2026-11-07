import numpy as np

def get_fft_half_mag(fft):
    length = len(fft)
    fft_half = fft[:length // 2]
    fft_half_mag = np.abs(fft_half)
    return fft_half_mag

def chirp_range_fft(chirp):
    chirp_fft = np.fft.fft(chirp)
    chirp_fft_half_mag = get_fft_half_mag(chirp_fft)
    return chirp_fft, chirp_fft_half_mag

def frame_range_fft(frame):
    frame_fft = []
    frame_fft_half_mag = []
    for chirp in frame:
        chirp_fft, chirp_fft_half_mag = chirp_range_fft(chirp)
        frame_fft.append(chirp_fft)
        frame_fft_half_mag.append(chirp_fft_half_mag)
    return np.array(frame_fft), np.array(frame_fft_half_mag)