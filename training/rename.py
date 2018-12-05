
from PIL import Image
import os

for filename in os.listdir("."):
    if(filename.endswith(".txt")):
        os.rename(filename,filename[:-4]+".gt.txt")
        print(filename[:-4])
   
