import random

def makeDATimage(imageName):
    image = ""
    head = "P3 1280 800 255\n"

    file = open(imageName, 'w')
    file.write(head)

    for i in range(1280):
        for j in range(800):

            r = (i**j) % 256;
            g = (i**j) % 256;
            b = (i**j) % 256;

            r = (r * g * b) % 256;
            g = (r * g * b) % 256;
            b = (r * g * b) % 256;

            file.write("%d %d %d\n"%(r, g, b))
            
makeDATimage("ayy.ppm")
