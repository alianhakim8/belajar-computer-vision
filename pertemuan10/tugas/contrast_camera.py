import cv2

capture = cv2.VideoCapture(0)

while True:
    __, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    contrast = cv2.equalizeHist(gray)
    cv2.imshow('frame', contrast)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
