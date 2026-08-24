import sys
import csv
import os
from PIL import Image, ImageOps

def main():
    # Checking arguements
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguements")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguements")
    elif not sys.argv[1].endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid input")
    elif not sys.argv[2].endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")

    # Getting extensions of input and output
    name1, ext1 = os.path.splitext(sys.argv[1])
    name2, ext2 = os.path.splitext(sys.argv[2])

    # Checking if input and output have the same extension
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

    # Opening the given image and the shirt.png, resizing and pasting the shirt.png on top (Double paste to be transparent)
    try:
        first = Image.open(sys.argv[1])
        second = Image.open("shirt.png")
        size = second.size
        first_fit = ImageOps.fit(first, size)
        first_fit.paste(second, (0, 0), second)
        first_fit.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit(f"Could not find {sys.argv[1]}")


if __name__ == "__main__":
    main()