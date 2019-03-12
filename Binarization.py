import cv2

def nothing(x):
    pass
cv2.namedWindow('Binary')
cv2.createTrackbar('threshold','Binary',0,255,nothing)
cv2.setTrackbarPos('threshold','Binary',127) #초기값 지정
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    low = cv2.getTrackbarPos('threshold','Binary')
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret, img_binary =cv2.threshold(gray,low,255,cv2.THRESH_BINARY_INV) #threshold(2진화 할 이미지, 기준점,기준점을 넘을시 255,cv2.THRESH_BINARY)
    #cv2.THRESH_BINARY_INV = 흰색과 검정색 반전
    cv2.imshow('frame',img_binary)
    img_result = cv2.bitwise_and(frame,frame,mask=img_binary)
    cv2.imshow("Result",img_result)
    if cv2.waitKey(1)& 0xff == ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()