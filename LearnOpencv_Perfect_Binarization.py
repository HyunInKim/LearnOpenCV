import cv2
import time
import numpy as np

def WindowResize(src,x,y):              #윈도우 창 크기 조정
    return cv2.resize(src,(x,y))
def DefaultWindowResize(src):
    return cv2.flip(cv2.resize(src,(300,300)),1) #화면 좌우 반전 + 크기조정


cap = cv2.VideoCapture(0)
prevTime = 0
while(True):
    ret, hand = cap.read()
    #####ShowFPS###############################################################
    curTime = time.time()
    sec = curTime - prevTime
    prevTime = curTime
    fps = 1 / (sec)
    str = "FPS : %0.1f" % fps
    cv2.putText(hand, str, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
    ############################################################################
    HSV = cv2.cvtColor(hand,cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(hand,cv2.COLOR_BGR2GRAY)

    gaus = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,1)
    ret2, otsu = cv2.threshold(gray,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret3, threshold1 = cv2.threshold(gray,100,255,cv2.THRESH_TOZERO)



    ######모폴로지####
    kernel = np.ones((11,11),np.uint8)
    result = cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel)
    ret1, threshold = cv2.threshold(result, 124, 255, cv2.THRESH_BINARY)

    cv2.imshow("Morphlogy",result)
    cv2.imshow("Gray",DefaultWindowResize(gray))
    cv2.imshow("Main",DefaultWindowResize(hand))
    cv2.imshow("GlobalThreshold",DefaultWindowResize(threshold))
    cv2.imshow("Gausian",DefaultWindowResize(gaus))
    cv2.imshow("Otsu",DefaultWindowResize(otsu))
    cv2.imshow("threshold TOZERO",DefaultWindowResize(threshold1))







    if cv2.waitKey(1) & 0xff == ord('q'):  # q버튼을 누르면 영상 꺼짐
        break
cap.release()
cv2.destroyAllWindows()