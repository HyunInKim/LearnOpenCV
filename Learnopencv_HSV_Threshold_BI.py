import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read();
    height,width = frame.shape[:2]
    img_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue1 = np.array([122, 30, 30])
    upper_blue1 = np.array([122 + 10, 255, 255])
    lower_blue2 = np.array([122 - 10, 30, 30])
    upper_blue2 = np.array([122, 255, 255])
    lower_blue3 = np.array([122 - 10, 30, 30])
    upper_blue3 = np.array([122, 255, 255])

    img_mask1 = cv2.inRange(img_hsv, lower_blue1, upper_blue1)
    img_mask2 = cv2.inRange(img_hsv, lower_blue2, upper_blue2)
    img_mask3 = cv2.inRange(img_hsv, lower_blue3, upper_blue3)
    img_mask = img_mask1 | img_mask2 | img_mask3

    # 마스크 이미지로 원본 이미지에서 범위값에 해당되는 영상 부분을 획득합니다.
    img_result = cv2.bitwise_and(frame, frame, mask=img_mask)
    cv2.imshow("mask", img_mask)
    cv2.imshow("Result", img_result)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):  # q버튼을 누르면 영상 꺼짐
        break;

cap.release()
cv2.destroyAllWindows()

