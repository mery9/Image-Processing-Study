import numpy as np
import cv2 as cv

#Create empty image
img = np.zeros([750, 750], dtype=np.uint8)
image = cv.imread('sample.jpg')

x1, y1 = 300, 300
x2, y2 = 500, 325

cv.line(img, (x1, y1), (x2, y2), (255, 255, 255), 5)

#Define the kernel
kernel_size = 35
kernel = np.zeros((kernel_size, kernel_size))
kernel[int((kernel_size - 1) / 2), :] = np.ones(kernel_size)
kernel /= kernel_size

#Apply the motion blur effect using the convolution operation
blurred_img = cv.filter2D(image, -1, kernel)

#Display the original and blurred images
cv.imshow('Original', img)
cv.imshow('Motion Blur', blurred_img)
cv.imwrite('Classwork2_Week3_MakeLineOutput1.png', img)
cv.imwrite('Classwork2_Week3_MakeLineOutput2.png', blurred_img)

#Wait for a key to be pressed
cv.waitKey(0)

#Clean up
cv.destroyAllWindows()
