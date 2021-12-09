import cv2

img = cv2.imread('smile2.webp', 1)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_eye.xml'
)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mata = eye_cascade.detectMultiScale(
    gray_img,
    scaleFactor=1.2,
    minNeighbors=18
)

for x, y, w, h in mata:
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
