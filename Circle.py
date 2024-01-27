import numpy as np
import cv2 as cv
import math

# Create empty image
img = np.zeros([1000, 1000], dtype = np.uint8)

# User input circle placement
Yplacement = int(input("Set Y: "))
Xplacement = int(input("Set X: "))
CircleRad = int(input("Set Circle Size: "))
circle_boundary = 100
circle_border_size = 100

# Draw a circle
for y in range(0, 1000):
    for x in range(0, 1000):
        r = math.sqrt((Yplacement - y)**2 + (Xplacement - x)**2)
        if r <= CircleRad:
            img[y, x] = 255

# Draw a circle boundary only
for y in range(0, 1000):
    for x in range(0, 1000):
        r = math.sqrt((800 - y)**2 + (800 - x)**2)
        if r <= circle_boundary:
            img[y, x] = 255

for y in range(0, 1000):
    for x in range(0, 1000):
        r = math.sqrt((800 - y)**2 + (800 - x)**2)
        if r <= circle_boundary - 1:
            img[y, x] = 0



# for y in range(75, 125):
#     for x in range(50, 250):
#         img[y,x] = 255

# Display the image
cv.imshow('Drawing', img)

#Wait for kay to be press
cv.waitKey(0)

#Clean up
cv.destroyAllWindows()