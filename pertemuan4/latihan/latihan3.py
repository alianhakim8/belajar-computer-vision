import cv2 as cv
import numpy as np

image = cv.imread('../assets/img/kucing-oren-barbar.jpg', 0)

if image is None:
    print('Could not open or find the image')
    exit(0)

bright = 34

new_image = np.zeros(image.shape, image.dtype)

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        newVal = image[y, x] - bright
        if newVal > 255:
            newVal = 255
        new_image[y, x] = newVal

cv.imshow('image grayscale', image)
cv.imshow('Decrease Brightness Image', new_image)
cv.waitKey(0)
cv.destroyAllWindows()
