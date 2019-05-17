import numpy as np
import cv2


img = cv2.imread('map_grid_processed.jpeg',1)

dim=img.shape
clsize=100
x=dim[0]//clsize
y=dim[1]//clsize

op=[]

#cv2.imshow('image',img)
#cv2.waitKey(0)

cl = int(clsize / 2)


for i in range(x):
    row=[]
    for j in range(y):  
        k=i*clsize+cl
        j=j*clsize+cl  
        if(img[k,j,0]==0 and img[k,j,1]==0 and img[k,j,2]==254):
            row.append(1)
        else:
            row.append(0)

    op.append(row)
 

f=open("final_matrix","w")

for i in range(x):
    for j in range(y):
        f.write(str(op[i][j])+" ")
    f.write("\n")

f.close() 


