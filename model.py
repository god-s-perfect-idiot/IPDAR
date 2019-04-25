import numpy as np
import cv2

img=cv2.imread('map.jpeg')

factor=1

dim = img.shape

grid=np.zeros((int(dim[0])//factor,int(dim[1])//factor))
np.set_printoptions(suppress=True)


s_x,s_y=258,94

s_b,s_g,s_r=img[s_x][s_y][0],img[s_x][s_y][1],img[s_x][s_y][2]
f=0


for i in range(dim[0]):
    for j in range(dim[1]):
        
        k=0
        p_b,p_g,p_r=img[i][j][0],img[i][j][1],img[i][j][2]
        if(p_b==s_b):
            k+=1
        if(p_g==s_g):
            k+=1
        if(p_r==s_r):
            k+=1
        if(k!=3):
            f+=1


print(f)
np.savetxt('final_matrix',grid,'%5.3d')