import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread('download.jpg')

dim=(1000,768)
image=cv2.imread('download.jpg')
image=cv2.resize(image,dim)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.4, 5)
#print('Found{0}faces!'.format(len(faces)))
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('Faces found',image)
cv2.waitKey(0)