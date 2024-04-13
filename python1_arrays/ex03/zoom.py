from load_image import open_image
from PIL import Image

def print_imgInfo(img):
    '''Prints image dimensions and number of color channels, then prints every pixel value'''
    if isinstance(img.getpixel((0,0)), int):
        channels = 1
    else:
        channels = len(img.getpixel((0,0)))

    print(f"Dimensions:{img.width}x{img.height}  channels:{channels}")
    for x in range(img.height):
        for y in range(img.width):
            rgb = img.getpixel((y, x))
            print(f"pixel{x, y} {rgb}")


def cropping_dimensions(img) -> tuple:
    '''calculates the coordinates of the box in which to crop the image'''
    center_x = (img.width + 250) / 2
    center_y = (img.height - 170) / 2
    half_resize_scale = 200

    left = center_x - half_resize_scale
    right = center_x + half_resize_scale
    up = center_y - half_resize_scale
    down = center_y + half_resize_scale

    return (left, up, right, down)


def zoom_image() -> any:
    '''entry function that orchestrate the execution of the program, crops and discolor the image'''
    img = open_image()
    if img is None:
        return
    print_imgInfo(img)


    cropped_img = img.crop(cropping_dimensions(img))
    decolored_img = cropped_img.convert('L')
    decolored_img.show()

    print_imgInfo(decolored_img)

def main():
    zoom_image()

if __name__ == "__main__":
    main()