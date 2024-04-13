from PIL import Image

def open_image() -> any:
    '''Opens Frodo image and returns it'''
    try:
        img = Image.open("animal.jpeg")
    except IOError:
        print("Could not open Frodo image...")
        return None

    return img