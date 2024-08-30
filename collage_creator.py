"""
Module: collage_creator

A program to create an Andy Warhol-style collage.

Authors:
1) Name - USD Email Address
2) Name - USD Email Address
"""

import comp110_image

def copy_to(src_img, dest_img, start_x, start_y):
    """
    Copies one image into another, start at the given starting coordinate.

    DO NOT MODIFY THIS FUNCTION!!!

    Parameters:
    src_img (type: Picture) - The picture to copy.
    dest_img (type: Picture) - The picture to copy into.
    start_x (type: int) - The column where we start copying to dest_img.
    start_y (type: int) - The row where we start copying to dest_img.
    """
    for x in range(src_img.getWidth()):
        for y in range(src_img.getHeight()):
            srcPixel = src_img.getPixel(x,y)
            dest_img.setPixel(x + start_x, y + start_y, srcPixel)


def main():
    pass # Remove this line once you implement main


if __name__ == "__main__":
    main()
