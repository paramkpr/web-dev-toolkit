from PIL import Image
import os

PATH = "/mnt/c/Users/Param/Desktop/projects/curioed-frontend/curioed/public/img/icons/"
dir_list = os.listdir(PATH)

for i in dir_list:
    if i.endswith(".png"):
        image = Image.open(PATH + i)
        image.save(PATH + i.split('.')[0] + '.webp', format='WEBP')
