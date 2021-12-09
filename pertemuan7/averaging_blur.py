import cv2
import numpy as np

src = cv2.imread('kucing-oren.jpg', 1)

# apply averaging blur on src image
dst = cv2.blur(src, (2, 2))

# display input and output image
cv2.imshow("Averaging Smoothing", np.hstack((src, dst)))
cv2.waitKey(0)  # wait until a key is pressed
cv2.destroyAllWindows()  # destroy the window showing image
