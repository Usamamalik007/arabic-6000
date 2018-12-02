from PIL import Image
from resizeimage import resizeimage
import os

for filename in os.listdir("."):
    if filename.endswith(".jpg"):
        print filename
        # print(os.path.join(directory, filename))
        fd_img = open(filename, 'r+b')
        img = Image.open(fd_img)
        img = resizeimage.resize_height(img, 100)
        img.save(filename, img.format)
        fd_img.close()
        continue
        

    else:
        continue


