import cv2 as cv
import numpy as np

image = cv.imread('../assets/img/kucing-oren-barbar.jpg', 0)

new_image = np.zeros(image.shape, image.dtype)
constant = 0.5

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        new_val = image[y, x] * constant
        print(new_val)
        new_image[y, x] = new_val

cv.imshow("original image", image)
cv.imshow("decreasing contrast image", new_image)
cv.waitKey(0)
cv.destroyAllWindows()
