from load_image import open_image
from PIL import Image

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


def transform_image() -> any:
    '''entry function that orchestrate the execution of the program, crops and discolor and rotate the image'''
    img = open_image()
    if img is None:
        return

    cropped_img = img.crop(cropping_dimensions(img))
    decolored_img = cropped_img.convert('L')

    rotated_image = Image.new(mode="L", size=(decolored_img.width, decolored_img.height))

    for x in range(decolored_img.width):
        for y in range(decolored_img.height):
            rotated_image.putpixel(((y, x)),  decolored_img.getpixel((x, y)))

    rotated_image.show()




def main():
    transform_image()

if __name__ == "__main__":
    main()