import numpy as np
import matplotlib.pyplot as plt
from utils import *
from matrice_seuillage import *
from PIL import Image


def FloydErrDiffusion(img, matriceSeuilage):
    (height, width) = img.shape()
    #height = len(img)
    #width = len(img[0])
    for y in range(0, height):
        for x in range(0, width):
            valPx = val_px(img, x, y)
            newValPx = newValPixel(matriceSeuilage, img, x, y)
            error = valPx - newValPx
            (r1, g1, b1) = img.getpixel()
            #(r1, g1, b1) = (valPx, valPx, valPx)
            if x < width - 1 :
                (r, g, b) = (r1 + (7/16) * error, g1 + (7/16) * error, b1 + (7/16) * error)
                img.putpixel((x + 1, y), (r, g, b))
                #oldVal = img[x + 1, y][0]
                #img[x + 1, y][0] = oldVal + (7/16) * error
            if x > 0 and y < height - 1 :
                (r, g, b) = (r1 + (3/16) * error, g1 + (3/16) * error, b1 + (3/16) * error)
                img.putpixel((x - 1, y + 1), (r, g, b))
            if y < height -1 :
                (r, g, b) = (r1 + (5/16) * error, g1 + (5/16) * error, b1 + (5/16) * error)
                img.putpixel((x, y + 1), (r, g, b))
            if x < width - 1 and y < height - 1 :
                (r, g, b) = (r1 + (1/16) * error, g1 + (1/16) * error, b1 + (1/16) * error)
                img.putpixel((x + 1, y + 1), (r, g, b))

img = Image.open("../images/newmann.jpg")
#plt.imshow(img, cmap = 'Greys')
#img.show()
ms = bayer(8)
FloydErrDiffusion(img, ms)