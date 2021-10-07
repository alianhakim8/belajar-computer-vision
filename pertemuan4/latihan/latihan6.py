import cv2 as cv
import numpy as np

image = cv.imread('../assets/img/kucing-oren-barbar.jpg')
alpha = 1.0

b = image.copy()
b[:, :, 1] = 0
b[:, :, 2] = 0

g = image.copy()
g[:, :, 0] = 0
g[:, :, 2] = 0

r = image.copy()
r[:, :, 0] = 0
r[:, :, 1] = 0

contrast_b = np.clip((1 + alpha) * b - 128 * alpha, 0, 255).astype(np.uint8)
contrast_g = np.clip((1 + alpha) * g - 128 * alpha, 0, 255).astype(np.uint8)
contrast_r = np.clip((1 + alpha) * r - 127 * alpha, 0, 255).astype(np.uint8)

cv.imshow("original image", image)
cv.imshow("Blue", contrast_b)
cv.imshow("Green", contrast_g)
cv.imshow("Red", contrast_r)

cv.waitKey(0)
cv.destroyAllWindows()
