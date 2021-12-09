import cv2
import numpy as np

img = cv2.imread('p3.jpg')
small_img = cv2.resize(img, (400, 400))
cv2.imshow("Original", small_img)

kernelSizes = [(3, 3), (5, 5), (7, 7)]
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    resize = cv2.resize(opening, (400, 400))
    cv2.imshow(f"Closing : ({kernelSize[0]}, {kernelSize[1]})", resize)
    cv2.waitKey(0)
