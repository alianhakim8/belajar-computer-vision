import cv2

img = cv2.imread('../smile2.webp', 1)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_frontalface_default.xml'
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_eye.xml'
)

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_smile.xml'
)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

wajah = face_cascade.detectMultiScale(
    gray_img,
    scaleFactor=1.5,
    minNeighbors=2
)

mata = eye_cascade.detectMultiScale(
    gray_img,
    scaleFactor=1.2,
    minNeighbors=18
)

senyum = smile_cascade.detectMultiScale(
    gray_img,
    scaleFactor=2.5,
    minNeighbors=20
)

for x, y, w, h in wajah:
    img = cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        3
    )

for x, y, w, h in mata:
    img = cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (168, 50, 50),
        3
    )

for x, y, w, h in senyum:
    img = cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (209, 199, 4),
        3
    )

cv2.imshow('Gambar output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
