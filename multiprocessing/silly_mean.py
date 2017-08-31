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
data_chunks = np.array_split(data, 4)

p = multiprocessing.Pool(2)
sums= p.map(silly_sum, data_chunks)

print(sum(sum))

# --------------------
