import cv2 as cv
import numpy as np

image = cv.imread('../assets/img/kucing-oren-barbar.jpg')

b = image.copy()
b[:, :, 1] = 0
b[:, :, 2] = 0

g = image.copy()
g[:, :, 0] = 0
g[:, :, 2] = 0

r = image.copy()
r[:, :, 0] = 0
r[:, :, 1] = 0

new_image_b = np.zeros(b.shape, b.dtype)
new_image_g = np.zeros(g.shape, g.dtype)
new_image_r = np.zeros(r.shape, r.dtype)
constant = 0.5

for y in range(b.shape[0]):
    for x in range(b.shape[1]):
        for z in range(b.shape[2]):
            new_val = b[y, x, z] * constant
            new_image_b[y, x, z] = new_val

for y in range(g.shape[0]):
    for x in range(g.shape[1]):
        for z in range(g.shape[2]):
            new_val = g[y, x, z] * constant
            new_image_g[y, x, z] = new_val

for y in range(r.shape[0]):
    for x in range(r.shape[1]):
        for z in range(r.shape[2]):
            new_val = r[y, x, z] * constant
            new_image_r[y, x, z] = new_val

cv.imshow("original image", image)
cv.imshow("decreasing contrast blue", new_image_b)
cv.imshow("decreasing contrast green", new_image_g)
cv.imshow("decreasing contrast red", new_image_r)

cv.waitKey(0)
cv.destroyAllWindows()
