import numpy as np

# NAIF UNIFORME
def naif_uniforme():
    nu = '''0.5'''
    return np.matrix(nu)

# TRAME HORIZONTALE À POINT CENTRÉ BLANC
def horizontale_centree():
    hc8 = '''
    62 58 45 41 37 49 53 61;
    54 34 35 31 17 29 33 57;
    50 30 13  9  5 12 24 44;
    38 18  6  1  0  8 20 40;
    42 22 10  2  3  4 16 36;
    46 26 14  7 11 15 28 48;
    59 35 31 19 23 27 32 52;
    63 55 51 39 43 47 56 60
    '''
    return np.matrix(hc8)

# BAYER
def bayer_compatible(n):
    val = 2
    while(val < n):
        val = val*2
    return (val == n)

def bayer(n):
    B2 = np.matrix([[0,2],[3,1]])
    if not bayer_compatible(n):
        return np.empty((0,0))
    def aux(B, n):
        if(B.size == 2*n):
            return B
        else:
            U = np.ones(B.shape)
            a = 4*B + B2[0,0]*U
            b = 4*B + B2[0,1]*U
            c = 4*B + B2[1,0]*U
            d = 4*B + B2[1,1]*U
            line1 = np.concatenate((a, b), axis = 1)
            line2 = np.concatenate((c, d), axis = 1)
            new_B = np.concatenate((line1, line2), axis = 0)
            return aux(new_B, 2*n)
    return aux(B2, n)
