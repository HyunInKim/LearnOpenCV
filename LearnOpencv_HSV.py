#HSV 색공간에서 특정색 검출하기
def HSV():

    import numpy as np
    import cv2

    color = [255,0,0]
    pixel = np.uint8([[color]])

    hsv = cv2.cvtColor(pixel,cv2.COLOR_BGR2HSV)
    hsv = hsv[0][0]

    print("bgr: ",color)
    print("hsv: ",hsv)

import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()
    height,widht = frame.shape[:2]
    img_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowre_blue = (120-10,30,30)                      #원하는 색영역의 범위위
    upper_blue = (120+10,255,255)
    img_mask = cv2.inRange(img_hsv,lowre_blue,upper_blue)

    img_result = cv2.bitwise_and(frame,frame,mask=img_mask)
    cv2.imshow("mask",img_mask)
    cv2.imshow("Result",img_result)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):  # q버튼을 누르면 영상 꺼짐
        break;

cap.release()
cv2.destroyAllWindows()
