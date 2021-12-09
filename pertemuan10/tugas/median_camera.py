import cv2

capture = cv2.VideoCapture(0)

while True:
    __, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    medianBlur = cv2.medianBlur(gray, 9)

    cv2.imshow('frame', medianBlur)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
