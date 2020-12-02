#!/bin/usr/python3

import PIL.Image as Image
import PIL.ImageDraw as Draw
import sys

def main(args):
    args = ["obj.obj"]
    (points, areas) = readPoints(args[0])
    makeImage((normalizeToSize(points, 399),areas), mode="all")
    pass

def readPoints(fileName):
    file = open(fileName,"r")

    punkteliste = []
    flaechenliste = []

    for line in file.readlines():
        if line[0:2] == "v ":
            linechen = line[2:-1]
            # ["0.3", "", "", "", "1.3"]
            punkteliste.append(tuple(map(lambda x: float(x),filter(lambda x: x != "",linechen.split(' ')))))
            
        if line[0:2] == "f ":
            linechen = line[2:-1]
            triples = filter(lambda x: x!="", linechen.split(" "))
            tup = tuple(map(lambda x: int(x.split("/")[0]), triples))
            flaechenliste.append(tup)
    
    #print((punkteliste,flaechenliste))

    return (punkteliste,flaechenliste)

def normalizeToSize(unsereListe, normalizeTo):
    maxX = sorted(unsereListe, key=lambda x: x[0], reverse=True)[0][0]
    maxY = sorted(unsereListe, key=lambda x: x[1], reverse=True)[0][1]
    maxZ = sorted(unsereListe, key=lambda x: x[2], reverse=True)[0][2]
    minX = sorted(unsereListe, key=lambda x: x[0])[0][0]
    minY = sorted(unsereListe, key=lambda x: x[1])[0][1]
    minZ = sorted(unsereListe, key=lambda x: x[2])[0][2]
    scale = normalizeTo/max(maxX-minX,maxY-minY,maxZ-minZ)
    unsereListe = list(map(lambda x: (scale*(x[0]-minX), scale*(x[1]-minY), scale*(x[2]-minZ)), unsereListe))
    return unsereListe

def makeImage(liste, name="bild", mode ="xy"):
    im = Image.new("1", (400,400))
    draw = Draw.Draw(im)

    punkte = liste[0]
    flaechen = liste[1]


    if mode == "xy":
        for pixel in punkte:
            im.putpixel((int(pixel[0]),int(pixel[1])),1)
        for area in flaechen:
            # 1: (1,2,3)
            # 2: (3,3,3)
            # 3:(.,.,.)
            # 4: (100,120,120)
            # f1: (1,2,4) 
            # [(p1[x],p1[y]),(p2[x],p2[y]),(p4[x],p4[y])]        
            p1 = punkte[area[0]-1]
            p2 = punkte[area[1]-1]
            p3 = punkte[area[2]-1]
            print([(int(p1[0]),int(p1[1])),(int(p2[0]),int(p2[1])),(int(p3[0]),int(p3[1]))])
            draw.polygon([(int(p1[0]),int(p1[1])),(int(p2[0]),int(p2[1])),(int(p3[0]),int(p3[1]))], outline=128)
        im.save(name + ".png")
        return
    elif mode == "xz":
        for pixel in punkte:
            im.putpixel((int(pixel[0]),int(pixel[2])),1)
        for area in flaechen:
            p1 = punkte[area[0]-1]
            p2 = punkte[area[1]-1]
            p3 = punkte[area[2]-1]
            draw.polygon([(int(p1[0]),int(p1[2])),(int(p2[0]),int(p2[2])),(int(p3[0]),int(p3[2]))], outline=128)
        im.save(name + ".png")
        return
    elif mode == "yz":
        for pixel in punkte:
            im.putpixel((int(pixel[1]),int(pixel[2])),1)
        for area in flaechen:
            p1 = punkte[area[0]-1]
            p2 = punkte[area[1]-1]
            p3 = punkte[area[2]-1]
            draw.polygon([(int(p1[1]),int(p1[2])),(int(p2[1]),int(p2[2])),(int(p3[1]),int(p3[2]))], outline=128)
        im.save(name + ".png")
        return
    elif mode == "all":
        makeImage(liste, name+"xy", "xy")
        makeImage(liste, name+"xz", "xz")
        makeImage(liste, name+"yz", "yz")
        return

    
        


if __name__ == "__main__":
    main(sys.argv[1:])