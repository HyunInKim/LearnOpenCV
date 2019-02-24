import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)
# 5px 짜리 직선그리기 (시작점),(끝점),(색상),크기
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
# 3px 짜리 사각형 그리기 (시작점),(다음점),(색상),크기
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
# 꽉찬 원그리기 (중심점),반지름(색상),채우냐 마냐 -1 = 채우기 1 = 채우기x
img = cv2.circle(img,(447,63), 63, (0,0,255), -1) #원그리기
# 글자쓰기
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),1,cv2.LINE_AA)




cv2.imshow("Drawing",img)
k = cv2.waitKey(0)  # 키보드 눌림 대기
if k == 27:  # ESC키
    cv2.destroyAllWindows();

