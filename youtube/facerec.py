import cv2

img = cv2.imread('person.jpg', 1)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_frontalface_default.xml'
)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(
    gray_img,
    scaleFactor=1.5,
    minNeighbors=2
)

for x, y, w, h in face:
    img = cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        3
    )

cv2.imshow('output', img)
cv2.waitKey(0)
cv2.destroAllWindows()
