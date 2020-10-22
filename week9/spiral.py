import numpy as np

def spiral_ccw(A):                # _ccw = counter clockwise
    A = np.array(A)
    out = []
    while(A.size):
        out.append(A[0][::-1])    # [::-1] first row reversed
        A = A[1:][::-1].T         # cuts first row; rotates clockwise
    return np.concatenate(out)    # np.concatenate "joins a sequence of arrays along an existing axis"

def base_spiral(nrow, ncol):      # creates indices on spiral
    return spiral_ccw(np.arange(nrow*ncol).reshape(nrow,ncol))[::-1]

def to_spiral(A):                 # transforms matrix into spiral with same dimensions
    A = np.array(A)
    B = np.empty_like(A)          # returns a new array with the same shape and type as a given array
    B.flat[base_spiral(*A.shape)] = A.flat
    return B

B = np.arange(1,251002).reshape(501,501)
# replace with np.arange(1,26).reshape(5,5) or something similar for visible spiral in numpy

print(to_spiral(B))
# did not add diagonals
# used stackoverflow for help
# did not see starter code
