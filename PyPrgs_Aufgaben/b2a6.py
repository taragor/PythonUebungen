#!/bin/usr/python3
import PIL.Image as Image
import sys

def main(args):
    img = Image.open(args[1])
    cols, rows = img.size # 512, 512
    v = img.getpixel((cols-1, rows-1)) # hole Wert eines Pixel (0..255)
    img.putpixel((0,0), v) # setze Pixel von rechts unten nach links oben
    img2 = img
    for i in range(1, cols) :
        for j in range(0,rows):
            if img.getpixel((i-1, j-1)) <100:
                img2.putpixel((i-1, j-1), 0)
    img2.show()
    img.show()
    #img.save("/tmp/komisch.pgm")


if __name__ == "__main__":
    main(sys.argv[1:])