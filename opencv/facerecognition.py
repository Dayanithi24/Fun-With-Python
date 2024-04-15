import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)

while 1:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2,cv2.LINE_AA)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Daya',(200,200),font,2,(255,255,0),2,cv2.LINE_AA)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h, x:x+w]
    cv2.imshow('img',img)
    k=cv2.waitKey(30)
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
