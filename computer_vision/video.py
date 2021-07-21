import cv2

cap = cv2.VideoCapture(r"C:\Users\hp\Videos\videos\-_'___..!(360p).mp4")
while True:
    ret,frame = cap.read()
    if not ret:
        print("can't receive frame")
        break
    cv2.imshow("video",frame)
    if cv2.waitKey(2) == 27:  # if you press esc
        break

cap.release()
cv2.destroyAllWindows()