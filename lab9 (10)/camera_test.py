import cv2

vid = cv2.VideoCapture(0)

if not vid.isOpened():
    print("Nu se poate accesa camera")
    exit()

while True:
    ret, frame = vid.read()

    if not ret:
        print("Nu se poate citi frame-ul")
        break

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()