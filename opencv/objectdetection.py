import cv2
image=cv2.imread('ted_cruz.jpg')

image=cv2.resize(image,(500,700))
classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

coordinates=classifier.detectMultiScale(gray_image)
for (x,y,w,h) in coordinates:
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow('image',image)
while True:
	key=cv2.waitKey(1)
	if key==27:
		cv2.destroyAllWindows()
		break