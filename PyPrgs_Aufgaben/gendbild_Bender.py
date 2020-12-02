#!/usr/bin/python3
import sys
import string
import re
import PIL.Image as Image
import PIL.ImageDraw as Draw

def main():
    file = "einfachd.obj"

    objread(file)
    machebild(file,"dreieck","xy")

def objread(file):
    datei = open(file,"r")
    zeilen = [line.rstrip("\n") for line in datei.readlines()]
    punkte = []
    dreiecke = []

    for stelle in zeilen:
        if stelle.startswith("v"):
            punkte.append(tuple(map(lambda x: int(x),re.findall("\d+",stelle))))
        if stelle.startswith("f"):
            dreiecke.append(tuple(map(lambda x: int(x),re.findall("\d+",stelle))))
    
    return((punkte,dreiecke))

def machebild(file,name,mode):
    (punktel,dreickel) = objread(file)

    print(punktel)
    print(dreickel)  

    if mode == "xy":
        im = Image.new("1",(400,400))
        draw = Draw.Draw(im)
        for stelle in punktel:
            im.putpixel((int(stelle[0]),int(stelle[1])),1)
        for area in dreickel:
            p1 = punktel[area[0]-1] #p1 = 100,120,160 also stelle 0 von punktel, area[0]-1 = 1
            p2 = punktel[area[1]-1] #p2 = 210,170,180 also stelle 1 von punktel, area[1]-1 = 2
            p3 = punktel[area[2]-1] #p3 = 170,100,130 also stelle 3 von punktel (weil f an stelle 3 = 4), area[1]-1 = 4 
            #-1 weil in der datei bei 1 angefangen wird zu zählen
            draw.polygon([(p1[0],p1[1]),(p2[0],p2[1]),(p3[0],p3[1])],outline=128)
        im.save(name+"_xy.png")   
    elif mode == "xz":
        im = Image.new("1",(400,400))
        draw = Draw.Draw(im)
        for stelle in punktel:
            im.putpixel((int(stelle[0]),int(stelle[2])),1)
        for area in dreickel:
            p1 = punktel[area[0]-1] 
            p2 = punktel[area[1]-1]
            p3 = punktel[area[2]-1]
            draw.polygon([(p1[0],p1[2]),(p2[0],p2[2]),(p3[0],p3[2])],outline=128)
        im.save(name+"_xz.png")    
    elif mode == "yz":
        im = Image.new("1",(400,400))
        draw = Draw.Draw(im)
        for stelle in punktel:
            im.putpixel((int(stelle[1]),int(stelle[2])),1)
        for area in dreickel:
            p1 = punktel[area[0]-1] 
            p2 = punktel[area[1]-1]
            p3 = punktel[area[2]-1]
            draw.polygon([(p1[1],p1[2]),(p2[1],p2[2]),(p3[1],p3[2])],outline=128)
        im.save(name+"yz.png")
    elif mode == "all":
        machebild(file,"dreieck","xy")
        machebild(file,"dreieck","xz")
        machebild(file,"dreieck","yz")



if __name__ == "__main__":
    main()