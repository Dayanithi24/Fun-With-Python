import cv2
img=cv2.imread('form1.webp')
res=cv2.resize(img,None,fx=2,fy=2)
cv2.imshow("Oringinal image",img)
cv2.imshow("Resized image",res)
cv2.waitKey(5000)
cv2.destroyAllWindows()