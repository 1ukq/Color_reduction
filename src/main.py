import matplotlib.pyplot as plt
import matplotlib.image as mpllimg
import numpy as np
import os

from utils import *
from matrice_seuillage import *
from errorDiffusion import *

# PARAMETRES
num_image = 1
error_diffusion = True
ms = bayer(8)

# IMAGE LIST
os.chdir("../images")
list_img = os.listdir()
list_img.sort()

# IMAGE TO MATRIX & MATRIX INFOS
img = mpllimg.imread(list_img[num_image])
h_img = len(img)
w_img = len(img[1])

# ERROR DIFFUSION
if(error_diffusion):
    img = FloydErrDiffusion(img, ms)

# CREATE NEW IMAGE
cr_img = np.zeros((1, w_img*ms.shape[1] + 1))
for i in range(h_img):
    print(i)
    line = np.zeros((ms.shape[0], 1))
    for j in range(w_img):
        m = px_to_matrix(ms, img, i, j)
        line = np.concatenate((line, m), axis = 1)
    cr_img = np.concatenate((cr_img, line), axis = 0)

# SHOW
plt.imshow(cr_img, cmap = 'Greys')
plt.show()
