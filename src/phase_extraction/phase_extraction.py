import numpy as np

def extract_phase_from_frame(frame_fft, bin_index):
    coefficients = frame_fft[:, bin_index]
    phase = np.arctan2(coefficients.imag, coefficients.real)     
    return phase  