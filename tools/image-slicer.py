import os, sys
import PIL
from PIL import Image


#print('hello')
#print("CWD:", os.getcwd())

cards = []

try:
    with Image.open("raw-images/BomberBoys-PNPv2-USLetter-20.png") as im:
        new_im = im.crop((20, 20, 400, 700))
        im.show()
        new_im.show()
        try:
            new_im.save("processed-images/card1.png")
        except (OSError, ValueError):
            print("File not saved")
            
        
except OSError:
    print("File not opened")