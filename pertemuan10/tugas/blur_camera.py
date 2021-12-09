import cv2

capture = cv2.VideoCapture(0)

while True:
    __, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.blur(gray, (10, 10))
    cv2.imshow('frame', blur)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
