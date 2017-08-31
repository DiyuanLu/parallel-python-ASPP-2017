import numpy as np
import timeit
import multiprocessing

N = 4096

def silly_sum(data):
    nrows, ncols = data.shape

    sums = 0
    for i in range(nrows):
        for j in range(ncols):
            sums += data[i, j]
    return sums

data = np.random.rand(N, N)


# -- YOUR CODE HERE --


# --------------------
