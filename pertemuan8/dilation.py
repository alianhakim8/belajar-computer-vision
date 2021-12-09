import cv2
import numpy as np

img = cv2.imread('j.jpg', 0)
small_img = cv2.resize(img, (300, 400))
cv2.imshow("Original", small_img)

for i in range(0, 3):
    dilated = cv2.dilate(img.copy(), None, iterations=i + 1)
    img_resize = cv2.resize(dilated, (300, 400))
    cv2.imshow(f"Dilation ke {i + 1}", img_resize)

    cv2.waitKey(0)
