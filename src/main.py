import matplotlib.pyplot as plt
import matplotlib.image as mpllimg
import numpy as np
import os
from utils import *

# IMAGE LIST
os.chdir("../images")
list_img = os.listdir()
list_img.sort()

# IMAGE TO MATRIX & MATRIX INFOS
img = mpllimg.imread(list_img[2])
h_img = len(img)
w_img = len(img[1])

# MATRCES DE SEUILLAGE
ms_centree = '''
62 58 45 41 37 49 53 61;
54 34 35 31 17 29 33 57;
50 30 13  9  5 12 24 44;
38 18  6  1  0  8 20 40;
42 22 10  2  3  4 16 36;
46 26 14  7 11 15 28 48;
59 35 31 19 23 27 32 52;
63 55 51 39 43 47 56 60
'''
ms = np.matrix(ms_centree)

# CREATE BIG MATRIX
cr_img = np.zeros((1, w_img*ms.shape[1] + 1))
for i in range(h_img):
    print(i)
    line = np.zeros((ms.shape[0], 1))
    for j in range(w_img):
        m = px_to_matrix(ms, img, i, j)
        line = np.concatenate((line, m), axis = 1)
    cr_img = np.concatenate((cr_img, line), axis = 0)

plt.imshow(cr_img, cmap = 'Greys')
plt.show()

# SHOW
plt.imshow(img)
plt.show()
