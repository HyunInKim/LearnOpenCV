import cv2
import numpy as np
from matplotlib import pyplot as plt
from pynput.mouse import Controller

def mouse_callback(event,x,y,flags,param):
    print("X= "+str(x)+"Y= "+str(y))


img_rgb = cv2.imread('hand.jpg')
img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
temp = cv2.imread('handtemp2.jpg')
temp_gray = cv2.cvtColor(temp,cv2.COLOR_BGR2GRAY)
w,h = temp_gray.shape[::-1]

res = cv2.matchTemplate(img_gray,temp_gray,cv2.TM_CCOEFF_NORMED)
min_val, max_val,min_loc,max_loc = cv2.minMaxLoc(res)
print(min_val,max_val,min_loc,max_loc)


threshold = 0.9
loc = np.where(res >= threshold)

for pt in zip(*loc[::1]):
    cv2.rectangle(img_rgb,pt,(pt[0] + w,pt[1]+h),(0,255,255),2)
print(w)
print(res)
cv2.namedWindow('result')
cv2.setMouseCallback('result',mouse_callback)
cv2.imshow("test2",img_gray)
cv2.imshow("test",temp_gray)
cv2.imshow("result",img_rgb)
k = cv2.waitKey(0)  # 키보드 눌림 대기
if k == 27:  # ESC키
    cv2.destroyAllWindows();