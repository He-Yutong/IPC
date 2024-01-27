import cv2
def face_detect_method(img):
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
    face_detector=cv2.CascadeClassifier("D:/anaconda/envs/hyt/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml")
    face=face_detector.detectMultiScale(gray_img)
    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv2.imshow("result",img)

cap=cv2.VideoCapture(0)
while True:
    flag,frame=cap.read()
    if not flag:
        break
    face_detect_method(frame)
    if ord(' ')==cv2.waitKey(1):
        break
        
cv2.destroyAllWindows()
cap.release()