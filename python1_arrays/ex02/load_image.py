#!/usr/bin/python3
import numpy as np
from PIL import Image

def ft_load(path: str) -> any:
    '''Opens image from file path inputed and prints its size and each individual pixel rgb value'''

    try:
        img = Image.open(path)
    except IOError:
        print("Could not open the file.")
        return None
        

    print(img.format)
    for x in range(img.height):
        for y in range(img.width):
            rgb = img.getpixel((y, x))
            print(f"pixel{x, y} r:{rgb[0]}, g:{rgb[1]}, b:{rgb[2]}")
    return img

