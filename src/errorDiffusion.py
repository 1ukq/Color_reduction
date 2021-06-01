import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
from utils import *
from matrice_seuillage import *
from PIL import Image


def FloydErrDiffusion(img, matriceSeuilage):
    print("Preparing error diffusion...")
    width = len(img)
    height = len(img[0])
    imgC = np.copy(img)
    for y in range(0, height):
        for x in range(0, width):
            valPx = val_px(imgC, x, y)
            newValPx = newValPixel(matriceSeuilage, imgC, x, y)
            error = valPx - ((newValPx * 255)/(matriceSeuilage.max()+1))
            if x < width - 1 :
                newValErr = val_px(imgC, x+1, y) + (7/16) * error
                imgC[x+1, y] = (newValErr, newValErr, newValErr)
            if x > 0 and y < height - 1 :
                newValErr = val_px(imgC, x-1, y+1) + (3/16) * error
                imgC[x-1, y+1] = (newValErr, newValErr, newValErr)
            if y < height -1 :
                newValErr = val_px(imgC, x, y+1) + (5/16) * error
                imgC[x, y+1] = (newValErr, newValErr, newValErr)
            if x < width - 1 and y < height - 1 :
                newValErr = val_px(imgC, x+1, y+1) + (1/16) * error
                imgC[x+1, y+1] = (newValErr, newValErr, newValErr)
    return imgC

#img = Image.open("../images/newmann.jpg")
#plt.imshow(img, cmap = 'Greys')
#img.show()
#ms = bayer(8)
#FloydErrDiffusion(img, ms)

#img = image.imread("../images/newmann.jpg")
#print(len(img))
#print(len(img[0]))
#imgC = FloydErrDiffusion(img, bayer(8))
#plt.imshow(imgC)
#plt.show()
