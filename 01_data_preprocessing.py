import numpy as np
import pandas as pd
from scipy.signal import butter, filtfilt

def butter_lowpass_filter(data, cutoff=25, sampling_rate=1000, order=4):
    """
    Applies a 4th-order low-pass Butterworth filter to raw kinetic data.
    """
    nyquist = 0.5 * sampling_rate
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

def calculate_asymmetry_index(peak_affected, peak_unaffected):
    """
    Calculates the Inter-Limb Load Asymmetry Index (%):
    |Peak_Affected - Peak_Unaffected| / [(Peak_Affected + Peak_Unaffected) / 2] * 100
    """
    numerator = np.abs(peak_affected - peak_unaffected)
    denominator = (peak_affected + peak_unaffected) / 2.0
    return (numerator / denominator) * 100.0

if __name__ == "__main__":
    print("Data preprocessing module ready.")