import numpy as np
import cv2

cap = cv2.VideoCapture(0)
color = [255,0,0]
pixel = np.uint8([[color]])

hsv = cv2.cvtColor(pixel,cv2.COLOR_BGR2HSV)
hsv = hsv[0][0]

print("bgr: ",color)
print("hsv: ",hsv)
while(True):
    ret,frame = cap.read()
    height,widht = frame.shape[:2]
    img_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv",img_hsv)
    if cv2.waitKey(1) & 0xff == ord('q'):  # q버튼을 누르면 영상 꺼짐
        break;

cap.release()
cv2.destroyAllWindows()
