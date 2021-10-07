import cv2
import numpy as np

image = cv2.imread('../assets/img/kucing-oren-barbar.jpg')
if image is None:
    print('Could not open or find the image. ')
    exit(0)

new_image = np.zeros(image.shape, image.dtype)
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        new_image[y, x] = 255 - image[y, x]

cv2.imshow('Original image', image)
cv2.imshow('Negative image', new_image)
cv2.waitKey()
