import cv2

img = cv2.imread('stop_3.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

stop_data = cv2.CascadeClassifier('stop_data.xml')

found = stop_data.detectMultiScale(img,
                                   minSize=(20, 20))

amount_found = len(found)

if amount_found != 0:
    for (x, y, width, height) in found:
        cv2.rectangle(img, (x, y),
                      (x + height, y + width),
                      (0, 255, 0), 5)

cv2.imshow("stop sign", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
