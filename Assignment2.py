import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_gamma_correction(block, gamma):
    gamma_corrected = np.power(block / 255.0, gamma) * 255.0
    gamma_corrected = np.clip(gamma_corrected, 0, 255).astype(np.uint8)
    return gamma_corrected

def process_image(image_path, window_size, overlap, mean_threshold, gamma1, gamma2):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    height, width = image.shape[:2]
    stride = window_size - overlap
    gamma_corrected_image = np.zeros_like(image)

    for y in range(0, height-window_size+1, stride):
        for x in range(0, width-window_size+1, stride):
            block = image[y:y+window_size, x:x+window_size]
            mean_value = np.mean(cv2.calcHist([block], [0], None, [256], [0, 256]))

            if mean_value < mean_threshold:
                gamma_corrected_block = apply_gamma_correction(block, gamma1)
            else:
                gamma_corrected_block = apply_gamma_correction(block, gamma2)

            gamma_corrected_image[y:y+window_size, x:x+window_size] = gamma_corrected_block

    plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original')
    plt.subplot(122), plt.imshow(gamma_corrected_image, cmap='gray'), plt.title('Gamma Corrected')
    plt.show()

image_path = 'IMG.tiff'
window_size = 64
overlap = 16
mean_threshold = 100
gamma1 = 0.7
gamma2 = 1.3

process_image(image_path, window_size, overlap, mean_threshold, gamma1, gamma2)