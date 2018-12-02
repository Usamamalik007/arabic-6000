from PIL import Image
from resizeimage import resizeimage
import os
import cv2
import numpy as np
from random import randint

aa=0
w=0
x=0
y=0
z=0

while aa<1000:
    w=randint(1, 525)
    x=randint(1, 525)
    y=randint(1, 525)
    z=randint(1, 525)
    print(str(w)+","+str(x)+","+str(y)+","+str(z)+",")
    img1 = cv2.imread(str(x)+'.jpg')
    img2 = cv2.imread(str(y)+'.jpg')
    img3 = cv2.imread(str(z)+'.jpg')
    img4 = cv2.imread(str(w)+'.jpg')	
               
    vis = np.concatenate((img1, img2,img3,img4), axis=1)
    cv2.imwrite("_"+str(x)+"_"+str(y)+"_"+str(z)+"_"+str(w)+'.jpg', vis)
    with open("_"+str(x)+"_"+str(y)+"_"+str(z)+"_"+str(w)+'.gt.txt', 'w',encoding="utf-8") as f:
        with open(str(x)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            a=myfile.read()
        with open(str(y)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            b=myfile.read()
        with open(str(z)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            c=myfile.read()
        with open(str(w)+'.gt.txt', 'r',encoding="utf-8") as myfile:
            d=myfile.read()

        f.write(str(d) + " "+str(c)+" "+str(b)+" "+str(a) )

        aa=aa+1


