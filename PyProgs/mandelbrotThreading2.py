import PIL.Image as Image
import cmath
import time
import multiprocessing

def main():
    start = time.process_time()
    mandelBrotSet(50, 5, -1.5, .5, -1, 1, 1000, 1000, "mandelbrot.png")
    print(time.process_time()-start)
    pass

def mandelBrotSet(iterations, divCrit, xMin, xMax, yMin, yMax, xRes, yRes, imOutput):
    threadList = []
    plot = Image.new("L", (xRes, yRes))
    for x in range(0, xRes):
        re = x*((xMax-xMin)/xRes)+xMin
        #threadFunction(iterations, divCrit, complex(re,im), x, y, plot)
        threadList.append(multiprocessing.Process(target=threadFunction,args=(iterations, divCrit, re, x, yRes, yMin, yMax, plot)))
        threadList[-1].start()
        print(x)

    for thread in threadList:
        thread.join()
    plot.save(imOutput,"PNG")

def threadFunction(iterations, divCrit, re, xPix, yRes, yMin, yMax, image):
    for yPix in range(0, yRes):
        im = yPix*((yMax-yMin)/yRes)+yMin
        threadReturn = iterate(complex(re,im), iterations, divCrit)*(255/iterations)
        #print("Pixel", xPix, ":" ,yPix, " berechnet")
        pxl = int(threadReturn)
        image.putpixel((xPix,yPix), pxl)


def iterate(constant, iterations, divCrit):
    z = complex(0,0)
    i = 0
    while(i<iterations and abs(z)<=divCrit):
        z = z**2+constant
        i+=1
    if(i < iterations):
        return i
    else:
        return 0

if __name__ == "__main__":
    main()