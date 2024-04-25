from PIL import Image

def open_image() -> any:
    '''Opens image and returns it'''
    try:
        img = Image.open("animal.jpeg")
    except IOError:
        print("Could not open image...")
        return None

    return img