import cv2
import numpy as np



def mouse_callback(event,x,y,flags,param):
    print("X= "+str(x)+"Y= "+str(y))

img = cv2.imread('Ronaldo.jpg')
px = img[100,100] # 100,100 지점의 색상값 BGR
blue = img[100,100,0] #100,100 지점의 B 색상값만 반환 [x,y,0 = B , 1 = G, 2 = R]
img[100,100] = [255,255,255] #100,100 지점의 색상 변경하기.
img.item(10,10,2)
print(img.shape) #이미지의 크기
print(img.size) #이미지의 사이즈 즉 픽셀수
print(img.dtype) #이미지의 데이터 타입
ball = img[253:358, 62:155] #Y,X
img[153:258,62:155] = ball


cv2.namedWindow('image')
cv2.setMouseCallback('image',mouse_callback)


while(1):
    cv2.imshow("image",img);
    k = cv2.waitKey(0)  #키보드 눌림 대기
    if k == 27:# ESC키
        break;
cv2.destroyAllWindows();
