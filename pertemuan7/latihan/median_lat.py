import cv2
import numpy

# read image
src = cv2.imread('../kucing-oren.jpg', cv2.IMREAD_UNCHANGED)

# apply gaussian blue on src image
dst = cv2.medianBlur(src, 9)

# display input and output image
cv2.imshow('Median Smoothing', numpy.hstack((src, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()
