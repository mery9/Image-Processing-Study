import cv2 as cv
import random

img = cv.imread('sample.jpg', cv.IMREAD_GRAYSCALE)

density_salt = 0.4
density_pepper = 0.4

# Set number of white pixel (salt)
number_of_white_pixel = int(density_salt * (img.shape[0] * img.shape[1]))

# Add salt to the image
for i in range(number_of_white_pixel):
    y_coord = random.randint(0, img.shape[0] - 1)
    x_coord = random.randint(0, img.shape[1]- 1)
    img[y_coord][x_coord] = 255

# Set number of black pixel (pepper)
number_of_black_pixel = int(density_pepper * (img.shape[0] * img.shape[1]))

# Add pepper to the image
for i in range(number_of_black_pixel):
    y_coord = random.randint(0, img.shape[0] - 1)
    x_coord = random.randint(0, img.shape[1] - 1)
    img[y_coord][x_coord] = 0

cv.imwrite('ImageWithSaltPepper.png', img)


#Fix the image
#Load the image
image = cv.imread('ImageWithSaltPepper.png')

#Apply filter
filtered_image = cv.medianBlur(image, 13)  # Adjust the kernel size as needed แต่ต้องเป็นเลขคี่เท่านั้นจะได้สามารถหาค่ามัธยฐานที่เหมาะได้

#Display the original and filtered images
cv.imshow('Original Image', image)
cv.imshow('Filtered Image', filtered_image)
cv.imwrite('ImageWithSaltPepperErased.png', filtered_image)
cv.waitKey(0)
cv.destroyAllWindows()
