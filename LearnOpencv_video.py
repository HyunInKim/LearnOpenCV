import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #BGRCOLOR - > GRAY

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xff == ord('q'): #q버튼을 누르면 영상 꺼짐
        break;

cap.release()
cv2.destroyAllWindows()