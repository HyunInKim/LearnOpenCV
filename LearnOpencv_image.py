import cv2

img = cv2.imread('Test.jpg'); #이미지 불러오기
cv2.imshow("image",img); #이미지 보여주기 (윈도우창 이름, 불러온 이미지)
k = cv2.waitKey(0)  #키보드 눌림 대기
if k == 27:# ESC키
    cv2.destroyAllWindows();
elif k == ord('s'): #저장하기 버튼
    cv2.imwrite("test2.png",img)
    cv2.destroyAllWindows();
    