import numpy as np

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
