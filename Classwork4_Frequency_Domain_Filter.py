import cv2
import numpy as np
from matplotlib import pyplot as plt

# Step 1: สร้าง Sobel Filter (Horizontal) in Spatial Domain
sobel_filter_horizontal = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

# Step 2: แปลงรูป input ไป Frequency Domain พร้อมแสดงผลลัพธ์
input_image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)
frequency_domain_input = np.fft.fft2(input_image)

# แสดงผลลัพธ์ของรูป input และผลลัพธ์ของ frequency domain
plt.subplot(2, 3, 1), plt.imshow(input_image, cmap='gray')
plt.title('Original Image', fontsize=10), plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 2), plt.imshow(np.log(1 + np.abs(frequency_domain_input)), cmap='gray')
plt.title('Frequency Domain (Input Image)', fontsize=8), plt.xticks([]), plt.yticks([])

# Step 3: แปลง Sobel Filter ไปเป็น Frequency Domain พร้อมแสดงผลลัพธ์
frequency_domain_sobel = np.fft.fft2(sobel_filter_horizontal, s=frequency_domain_input.shape)

# แสดงผลลัพธ์ของ Sobel filter ใน frequency domain
plt.subplot(2, 3, 3), plt.imshow(np.log(1 + np.abs(frequency_domain_sobel)), cmap='gray')
plt.title('Frequency Domain (Sobel Filter)', fontsize=8), plt.xticks([]), plt.yticks([])

# Step 4: คูนจุดต่อจุด (Dot Product) ใน Frequency Domain พร้อมแสดงผลลัพธ์
filtered_image_frequency = frequency_domain_input * frequency_domain_sobel

# แสดงผลลัพธ์ของ Dot product ใน frequency domain
plt.subplot(2, 3, 4), plt.imshow(np.log(1 + np.abs(filtered_image_frequency)), cmap='gray')
plt.title('Frequency Domain (Dot Product Result)', fontsize=8), plt.xticks([]), plt.yticks([])

# Step 5: นำผลลัพธ์มา Convert กลับเป็น Spatial Domain และแสดงผลลัพธ์
filtered_image_spatial = np.fft.ifft2(filtered_image_frequency)
filtered_image_spatial = np.abs(filtered_image_spatial)

# แสดงผลลัพธ์ของรูป filter ใน Spatial Domain
plt.subplot(2, 3, 5), plt.imshow(filtered_image_spatial, cmap='gray')
plt.title('Filtered Image (Spatial Domain)', fontsize=8), plt.xticks([]), plt.yticks([])

# Step 6: เปรียบเทียบผลลัพธ์ระหว่าง Spatial กับ Frequency Domain พร้อมแสดงผล
filtered_image_spatial_domain = cv2.filter2D(input_image, -1, sobel_filter_horizontal)

# แสดงผลลัพธ์ของ Spatial กับ Frequency Domain
plt.subplot(2, 3, 6), plt.imshow(filtered_image_spatial_domain, cmap='gray')
plt.title('Filtered Image (Frequency Domain)', fontsize=8), plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()
