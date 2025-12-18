import numpy as np

def fft(signal):
    return np.fft.fft(signal)

# usage examples
signal = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
fft_result = fft(signal)
print("Hasil FFT:")
print(fft_result)