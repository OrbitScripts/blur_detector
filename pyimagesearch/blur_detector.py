import numpy as np


def detect_blur_fft(image, size=60):
    (h, w) = image.shape
    (cX, cY) = (int(w / 2.0), int(h / 2.0))
    fft = np.fft.fft2(image)
    fft_shift = np.fft.fftshift(fft)
    fft_shift[cY - size:cY + size, cX - size:cX + size] = 0
    fft_shift = np.fft.ifftshift(fft_shift)
    recon = np.fft.ifft2(fft_shift)
    np.seterr(divide='ignore')
    magnitude = 20 * np.log(np.abs(recon))
    mean = np.mean(magnitude)
    if mean == float("inf") or mean == float("-inf") or mean == float("+inf"):
        mean = 0

    return mean
