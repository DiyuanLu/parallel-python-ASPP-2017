import numpy as np
import timeit
import multiprocessing
import functools

from multiprocessing.sharedctypes import RawArray

N = 4096
buf = RawArray('d', N*N)

def silly_sum(nrows, start_row):
    data = np.frombuffer(buf)
    data = data.reshape([N, N])

    sums = 0
    for i in range(start_row, start_row+nrows):
        for j in range(N):
            sums += data[i, j]
    return sums

data = np.frombuffer(buf)
data = data.reshape([N, N])
data[...] = np.random.rand(N, N)

silly_sum_wrapped = functools.partial(silly_sum, N//4)
p = multiprocessing.Pool(4)
sums = p.map(silly_sum_wrapped, range(0, N, N//4))

print(sum(sums)/data.size)
