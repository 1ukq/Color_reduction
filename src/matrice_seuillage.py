import numpy as np

# HORIZONTALE
def horizontale():
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

# DIAGONALE
def diagonale():
    d8 = '''
    11 27 17 29 37 53 43 35;
    23  1  7 13 51 61 59 41;
    15  5  3 21 47 57 63 49;
    31 19 25  9 33 45 55 38;
    39 54 44 32  8 24 18 30;
    48 62 56 46 20  2  4 14;
    40 58 60 50 12  6  0 22;
    34 42 52 36 28 16 26 10
    '''
    return np.matrix(d8)

# NAIF
def naif(seuil):
    return seuil

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
