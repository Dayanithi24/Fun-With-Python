import cv2
import numpy as np
from numpy import single

img=cv2.imread('ted_cruz.jpg')
input_points=np.float32([[120,110],[655,162],[123,1002],[760,917]])

width=400
height=int(width*1.414)

converted_points=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(input_points,converted_points)
img_output = cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow('Original', img)
cv2.imshow('Wrapped perspective',img_output)



cv2.waitKey(0)