import cv2 as cv
import numpy as np

def draw_circle_on_non_white_pixels(image_input):
    #Read image input
    image = cv.imread(image_input)

    #Create a mask of every pixel that's non-white pixels
    mask = cv.inRange(image, (0, 0, 0), (200, 200, 200))

    #Find the indices of non-white pixels หาพื่นที่ ที่ไม่ใช่สีขาว
    non_white_indices = np.transpose(np.nonzero(mask))

    #Draw circles on non-white pixels
    for y, x in non_white_indices:
        cv.circle(image, (x, y), 28, (0, 0, 0), 56)

    #Display the resulting image
    cv.imshow('Circles on Non-White Pixels', image)
    cv.imwrite('Middle of The Circle.png', image)
    cv.waitKey(0)
    cv.destroyAllWindows()


image_input = 'Circle Objects2.png'
draw_circle_on_non_white_pixels(image_input)

