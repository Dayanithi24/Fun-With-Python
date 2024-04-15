import cv2
img=cv2.imread('form1.webp',1)
print(img)
cv2.imshow('form1.webp',img)
cv2.imwrite("learn.png",img)
cv2.waitKey(5000)
cv2.destroyAllWindows()