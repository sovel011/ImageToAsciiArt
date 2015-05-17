#!/usr/bin/env python3

import Image
import sys
import random

IMG_SIZE = 640, 480


charRamp = ['@', '#', '%', '*', '+', '=', '-', ':', '.', '`', '&nbsp;']
#charRamp = ['@', '%', '*', '+', '=', '-', '.', ' ']


def getChar(average):
    
    noise = random.randint(-10,10)
    #average += noise
    if (average > 255):
        return ' '
    if (average < 0):
        return '@'
    index = float(average / 255.0) * (len(charRamp))
    char = charRamp[int(index)]
    return char


if __name__ == '__main__':
    
    if (len(sys.argv) != 2):
        print 'Specify filename'
        exit()
    random.seed()
    filename = sys.argv[1]
    
    image = Image.open(filename)
    im = image.copy()
    pix = im.load()
    
    size = im.size #width, height
    
    for i in range (0, size[0]):
        for j in range (0, size[1]):
            pixel = pix[i, j]
            luminosity = int(pixel[0]*.21 + pixel[1]*.72 + pixel[2]*.07)
            pix[i,j] = (luminosity, luminosity, luminosity)

    im = im.resize(IMG_SIZE, Image.ANTIALIAS)
    pix = im.load()
    file = open("output.html", "w")

    file.write("<!DOCTYPE HTML>\n")
    file.write("<html><head><meta charset='UTF-8'>" +
               "<link rel='stylesheet' href='style.css'></head><body><p>")

    for i in range (0, 120):
        for j in range (0, 320):
            sum = 0
            for m in range (i*4, (i+1)*4):
                for n in range (j*2, (j+1)*2):
                    #print '\nm : ' + str(m)
                    #print '\nn : ' + str(n)
                    sum += pix[n,m][0]
            average = sum /8
            char = getChar(average)
            file.write(char)
        file.write("<br>")

    file.write("</p></body>")

#im.show()
    
    del image

