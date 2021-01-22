import PIL.Image as Image
import multiprocessing
import cmath
import time

def main():
    start = time.process_time()
    mandelBrotSet(50, 5, -1.5, .5, -1, 1, 8000, 8000, "mandelbrot.png")
    print(time.process_time()-start)
    pass

def mandelBrotSet(iterations, divCrit, xMin, xMax, yMin, yMax, xRes, yRes, imOutput):
    plot = Image.new("L", (xRes, yRes))
    threads = []
    rowsPerThread = int(yRes/8)
    for x in range(0, xRes, rowsPerThread):
        threads.append(multiprocessing.Process(target= calcRows, args=(iterations, divCrit, xMin, xMax, yMin, yMax, xRes, yRes, imOutput, x, x+rowsPerThread, plot)))
        threads[-1].start()
        print(x)
    print("------------------")
    for thread in threads:
        thread.join()
    plot.save(imOutput,"PNG")

def calcRows(iterations, divCrit, xMin, xMax, yMin, yMax, xRes, yRes, imOutput, xStart, xEnd, plot):
    for x in range(xStart, xEnd):
        for y in range(0, yRes):
            re = x*((xMax-xMin)/xRes)+xMin
            im = y*((yMax-yMin)/yRes)+yMin
            iterate(complex(re,im), iterations, divCrit, plot, (x,y), color)
            if x%50==0 and y==0:
                print(x)


def iterate(constant, iterations, divCrit, plot, targetPx, colorMap):
    z = complex(0,0)
    i = 0
    while(i<iterations and abs(z)<=divCrit):
        z = z**2+constant
        i+=1
    if(i < iterations):
        plot.putpixel(targetPx, colorMap(i, iterations))
    else:
        plot.putpixel(targetPx, 0)



def color(iterations, iterationsMax):
    return int(iterations*255/iterationsMax)

if __name__ == "__main__":
    main()