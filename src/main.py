import matplotlib.pyplot as plt
import matplotlib.image as mpllimg
import numpy as np
import os

from utils import *
from matrice_seuillage import *
from errorDiffusion import *

# PARAMETRES
num_image = 1
error_diffusion = False
ms = bayer(8)

# IMAGE LIST
os.chdir("../images")
list_img = os.listdir()
list_img.sort()

# IMAGE TO MATRIX & MATRIX INFOS
img = mpllimg.imread(list_img[num_image])

# ERROR DIFFUSION
if(error_diffusion):
    img = FloydErrDiffusion(img, ms)

# CREATE NEW IMAGE
cr_img = reduce_color(img, ms)

# SHOW
plt.imshow(cr_img, cmap = 'Greys')
plt.show()

plt.imshow(img, cmap = 'Greys')
plt.show()
