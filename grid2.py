import numpy as np
import cv2


img = cv2.imread('map.jpeg',1)

dim=img.shape
clsize=100
x=dim[0]//clsize
y=dim[1]//clsize


x_d=clsize
for i in range(x):
    cv2.line(img, (0,x_d),(dim[1],x_d),(0,0,0),2)
    x_d+=clsize

y_d=clsize
for i in range(y):
    cv2.line(img, (y_d,0),(y_d,dim[0]),(0,0,0),2)
    y_d+=clsize


cv2.imwrite('map_grid.jpeg',img)
