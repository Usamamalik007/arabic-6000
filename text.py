import numpy as np
from PIL import Image
import glob
import os

# images_list = [f for f in glob.glob("mst_wrd/*")]
i=1
for name in glob.glob('arabic/*'):
    
    for new in glob.glob(name+"/*.jpg"):
           print(str(i)+".jpg")
           
           os.rename(new,str(i)+".jpg")
           i=i+1

i=1
for name in glob.glob('arabic/*'):
    
    for new in glob.glob(name+"/*.txt"):
           print(str(i)+".txt")
           
           os.rename(new,str(i)+".txt")
           i=i+1


