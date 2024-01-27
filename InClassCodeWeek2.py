import numpy as np
import cv2 as cv

import matplotlib.pyplot as plt

img = cv.imread('sample.jpg')

#Convert color image to gray-scale image
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Calculate histogram of image
histogram = cv.calcHist([img_gray],[0], None, [256], [0, 256])

#Plot histogram with matplotlib
plt.plot(histogram, color='k')

plt.xlim([0, 256])
plt.grid(True)

plt.title('Histogram of Image')
plt.ylabel('Number of Pixels')
plt.xlabel('Intensity Levels')

plt.show()

