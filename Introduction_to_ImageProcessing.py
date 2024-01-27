import cv2 as cv

#Read Image file
img = cv.imread("IMG.tiff")

#Read Image file but make it greyscale
img = cv.imread("IMG.tiff", cv.IMREAD_GRAYSCALE)

#Data of the picture
print("Data type of image (Open CV): ", type(img))
print("Number of dimension: ", img.ndim)
print("Size of each dimension: ", img.shape)
print("image height: ", img.shape[0])
print("image width: ", img.shape[1])

#Display the image
cv.imshow("The image", img)

#Save the image
cv.imwrite("out.png", img)

#Wait for a key to be press
cv.waitKey(0)

#Clean up
cv.destroyAllWindows()


