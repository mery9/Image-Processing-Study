import cv2 as cv
import numpy as np

#Open Image
img_in = cv.imread('imgin.jpg', cv.IMREAD_GRAYSCALE)

#Apply Intensity transformation
gamma = 0.4
gamma_corrected = (img_in / 255)**gamma

#Scaling output
gamma_corrected = gamma_corrected*255

#Convert data type
img_out = np.array(gamma_corrected, dtype='uint8')

#Show image
cv.imshow("Power law", img_out)

#Save Output
cv.imwrite('Demo03_Pow_img2_input.png', img_in)
cv.imwrite('Demo03_Pow_img2_output.png', img_out)
