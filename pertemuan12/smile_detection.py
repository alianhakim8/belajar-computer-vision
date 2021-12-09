import cv2

img = cv2.imread('smile.jpg', 1)

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_smile.xml'
)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

senyum = smile_cascade.detectMultiScale(
    gray_img,
    scaleFactor=2.5,
    minNeighbors=20
)

for x, y, w, h in senyum:
    img = cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        3
    )

cv2.imshow('Gambar output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
