import cv2 as cv
import numpy as np

image = cv.imread('../assets/img/kucing-oren-barbar.jpg')

# set green and red channel to 0
b = image.copy()
b[:, :, 1] = 0
b[:, :, 2] = 0

# set blue and red channel to 0
g = image.copy()
g[:, :, 0] = 0
g[:, :, 2] = 0

r = image.copy()
r[:, :, 0] = 0
r[:, :, 1] = 0

if image is None:
    print('Could not open or find the image. ')
    exit(0)

bright = 50

new_image_b = np.zeros(b.shape, b.dtype)
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        for z in range(image.shape[2]):
            newVal = image[y, x, z] - bright
            if newVal > 255:
                newVal = 255
            new_image_b[y, x, z] = newVal

new_image_g = np.zeros(g.shape, g.dtype)
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        for z in range(image.shape[2]):
            newVal = image[y, x, z] - bright
            if newVal > 255:
                newVal = 255
            new_image_g[y, x, z] = newVal

new_image_r = np.zeros(r.shape, r.dtype)
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        for z in range(image.shape[2]):
            newVal = image[y, x, z] - bright
            if newVal > 255:
                newVal = 255
            new_image_r[y, x, z] = newVal

cv.imshow('image asli', image)
cv.imshow('Increase Brightness B-RGB', new_image_b)
cv.imshow('Increase Brightness G-RGB', new_image_g)
cv.imshow('Increase Brightness R-RGB', new_image_r)

cv.waitKey(0)
cv.destroyAllWindows()
