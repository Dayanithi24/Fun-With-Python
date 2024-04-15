import cv2
import numpy as np

dim=(500,768)
left=cv2.imread('Image0046_1.jpg')
left=cv2.resize(left,dim)

right=cv2.imread('Image0046_2.jpg')
right=cv2.resize(right,dim)



images=[]
images.append(left)
images.append(right)
cv2.imshow('Original1', left)
cv2.imshow('Original2', right)
stitchy=cv2.Stitcher.create()
ret,pano=stitchy.stitch(images)

if ret==cv2.STITCHER_OK:
    cv2.imshow('Panorama',pano)
    cv2.waitKey()
    cv2.destroyAllWindoes()
else:
    print('Error during Stitching')

