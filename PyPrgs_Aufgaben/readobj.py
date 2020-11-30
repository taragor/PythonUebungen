#!/bin/usr/python3

import PIL.Image as Image
import sys

def main(args):
    args = ["Box.obj"]
    file = open(args[0],"r")

    unsereListe = []

    for line in file.readlines():
        if line[0:2] == "v ":
            linechen = line[2:-1]
            unsereListe.append(tuple(map(lambda x: float(x),linechen.split(' '))))

    print(unsereListe)

    pass

def makeImage(liste, name ="bild", mode ="xy"):
    im = Image.new("1", (400,400))
    
        if mode == "xy":
            for pixel in liste:
                im.putpixel((pixel[0],pixel[1]),1)
        elif mode == "xz":
            for pixel in liste:
                im.putpixel((pixel[0],pixel[2]),1)
        else:
            for pixel in liste:
                im.putpixel((pixel[1],pixel[2]),1)


if __name__ == "__main__":
    main(sys.argv[1:])