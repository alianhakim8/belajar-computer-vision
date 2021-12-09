import cv2
import numpy

# read image
src = cv2.imread('kucing-oren.jpg', cv2.IMREAD_UNCHANGED)

# destination image
# apply gaussian blur on src image
dst = cv2.GaussianBlur(src, (5, 5), 0)

# display input and output image
cv2.imshow("Gaussian Smoothing", numpy.hstack((src, dst)))
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroy the window showing image
