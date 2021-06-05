import numpy as np

def val_px(img, x, y):
    return img[x,y][0]

def newValPixel(mat_ref, img, x, y):
    v = 1
    if(not isinstance(mat_ref, int)):
        # pas naif
        v = mat_ref.max() +1
    return round(val_px(img, x, y)*v/255)

def get_matrix(mat_ref, v):
    (h,w) = mat_ref.shape
    mat = np.zeros((h,w))
    for i in range(h):
        for j in range(w):
            if mat_ref[i,j] >= v:
                mat[i,j] = 1
    return mat

def px_to_matrix(mat_ref, img, x, y):
    v = newValPixel(mat_ref, img, x, y)
    return get_matrix(mat_ref, v)

def reduce_color(img, ms):
    print("Reducing...")
    h_img = img.shape[0]
    w_img = img.shape[1]

    if(isinstance(ms, int)):
        # cas de l'approche naive
        cr_img = np.zeros((h_img, w_img))
        seuil = ms
        for i in range(h_img):
            print("Line",i)
            for j in range(w_img):
                if(img[i,j][0] < seuil):
                    cr_img[i,j] = 1
        return cr_img

    # create first line
    cr_img = px_to_matrix(ms, img, 0, 0)
    for j in range(1, w_img):
        m = px_to_matrix(ms, img, 0, j)
        cr_img = np.concatenate((cr_img, m), axis = 1)

    for i in range(1, h_img):
        # create next line
        line = px_to_matrix(ms, img, i, 0)
        print("Line",i)
        for j in range(1, w_img):
            m = px_to_matrix(ms, img, i, j)
            # concat matrix to line
            line = np.concatenate((line, m), axis = 1)

        # concat line to cr_img
        cr_img = np.concatenate((cr_img, line), axis = 0)

    return cr_img
