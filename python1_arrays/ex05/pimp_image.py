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


def inverted_filter(original_rgb) -> tuple:
    return (255 - original_rgb[0], 255 - original_rgb[1], 255 - original_rgb[2])

def red_filter(original_rgb) -> tuple:
    return (original_rgb[0], 0, 0)

def blue_filter(original_rgb) -> tuple:
    return (0, original_rgb[1], 0)

def green_filter(original_rgb) -> tuple:
    return (0, 0, original_rgb[2])

def greyscale_filter(original_rgb) -> int:
    return 0.299 * original_rgb[0] + 0.587 * original_rgb[1] + 0.114 * original_rgb[2]

def apply_filter(img, filter):
    color_mode = "RGB"
    if filter == greyscale_filter:
        color_mode = "L"

    filtered_image = Image.new(mode=color_mode, size=(img.width, img.height))
    for x in range(img.width):
        for y in range(img.height):
            filtered_image.putpixel(((x, y)),  filter(img.getpixel((x, y))))
    filtered_image.show()

# def black_and_white_filter(img):
#     filtered_image = Image.new(mode="L", size=(img.width, img.height))
#     for x in range(img.width):
#         for y in range(img.height):
#             filtered_image.putpixel(((x, y)),  filter(img.getpixel((x, y))))

def pimp_image() -> any:
    '''entry function that orchestrate the execution of the program, crops and discolor the image'''
    img = open_image()
    if img is None:
        return
    
    img.show()
    apply_filter(img, inverted_filter)
    apply_filter(img, red_filter)
    apply_filter(img, blue_filter)
    apply_filter(img, green_filter)
    apply_filter(img, greyscale_filter)
    
    # for x in range(img.width):
    #     for y in range(img.height):
    #         img.putpixel(((y, x)),  img.getpixel((x, y)))

    # img.show()




def main():
    pimp_image()

if __name__ == "__main__":
    main()