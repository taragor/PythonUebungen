import PIL.Image as Image
import cmath
import time

def main():
    start = time.process_time()
    mandelBrotSet(1000, 100, -1.5, .5, -1, 1, 400, 400, "mandelbrot.png")
    print(time.process_time()-start)
    pass

def mandelBrotSet(iterations, divCrit, xMin, xMax, yMin, yMax, xRes, yRes, imOutput):
    plot = Image.new("L", (xRes, yRes))
    for x in range(0, xRes):
        for y in range(0, yRes):
            re = x*((xMax-xMin)/xRes)+xMin
            im = y*((yMax-yMin)/yRes)+yMin
            pxl = int(iterate(complex(re,im), iterations, divCrit)*(255/iterations))
            plot.putpixel((x,y), pxl)
            if y == 0 and x%10==0:
                print(x,y,pxl)
    plot.save(imOutput,"PNG")



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