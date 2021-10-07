import cv2 as cv
import numpy as np

image = cv.imread('../assets/img/kucing-oren-barbar.jpg')

if image is None:
    print('could not open or find the image')
    exit(0)

alpha = 1.0
contrast = np.clip((1+alpha)*image - 128*alpha, 0, 255).astype(np.uint8)

cv.imshow('original image', image)
cv.imshow('increase contrast', contrast)
cv.waitKey(0)
cv.destroyAllWindows()
