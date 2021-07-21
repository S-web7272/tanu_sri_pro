import cv2

font = cv2.FONT_HERSHEY_COMPLEX_SMALL

cap = cv2.VideoCapture(r"C:\Users\hp\Videos\videos\-_'___..!(360p).mp4")
while True:
    ret,frame = cap.read()
    
    if not ret:
        print("can't receive frame")
        break
    cv2.imshow("video",frame)
    cv2.rectangle(frame,(100,100),(300,300),(0,255,0),3)
    cv2.circle(frame,(300,300),100,(0,0,255,),2)
    cv2.putText(frame,'smita srivastava',(5,500),font,1,(255,0,255),4)
    cv2.imshow("drawing",frame)

    if cv2.waitKey(2) == 27:  # if you press esc
        break

cap.release()
cv2.destroyAllWindows()
