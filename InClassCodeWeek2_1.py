import numpy as np
import cv2 as cv

imgA = cv.imread('IMG.tiff', cv.IMREAD_GRAYSCALE)
imgB = cv.imread('HistEQ_After.png', cv.IMREAD_GRAYSCALE)

histB = cv.calcHist([imgB], [0], None, [256], [0,256])

imgAtoB = cv.equalizeHist(imgA, histB)

cv.imwrite('imgA.png', imgA)
cv.imwrite('imgB.png', imgB)
cv.imwrite('imgAtoB.png', imgAtoB)


