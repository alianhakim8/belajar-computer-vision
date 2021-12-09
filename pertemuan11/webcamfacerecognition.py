import cv2

capture = cv2.VideoCapture(1)

while True:
    __, frame = capture.read()

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        'haarcascade_frontalface_default.xml'
    )

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    wajah = face_cascade.detectMultiScale(
        gray_img,
        scaleFactor=1.5,
        minNeighbors=2
    )

    for x, y, w, h in wajah:
        img = cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )
    cv2.imshow('face', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
