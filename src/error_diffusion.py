from utils import *
from matrice_seuillage import *


def FloydErrDiffusion(img, matriceSeuillage):
    print("Preparing error diffusion...")
    width = len(img)
    height = len(img[0])
    imgC = np.copy(img)
    div = 1
    if(not isinstance(matriceSeuillage, int)):
        # n'est pas seuillage naif
        div = matriceSeuillage.max()+1
    for y in range(0, height):
        for x in range(0, width):
            valPx = val_px(imgC, x, y)
            newValPx = newValPixel(matriceSeuillage, imgC, x, y)
            error = valPx - ((newValPx * 255)/div)
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
