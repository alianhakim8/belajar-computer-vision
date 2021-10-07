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

new_image_b = np.zeros(b.shape, b.dtype)
for y in range(b.shape[0]):
    for x in range(b.shape[1]):
        new_image_b[y, x] = 255 - b[y, x]

new_image_g = np.zeros(g.shape, g.dtype)
for y in range(g.shape[0]):
    for x in range(g.shape[1]):
        new_image_g[y, x] = 255 - g[y, x]

new_image_r = np.zeros(r.shape, r.dtype)
for y in range(r.shape[0]):
    for x in range(r.shape[1]):
        new_image_r[y, x] = 255 - r[y, x]

cv.imshow('image asli', image)
cv.imshow('B-RGB', new_image_b)
cv.imshow('G-RGB', new_image_g)
cv.imshow('R-RGB', new_image_r)

cv.waitKey(0)
cv.destroyAllWindows()
