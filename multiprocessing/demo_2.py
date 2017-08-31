import multiprocessing
from multiprocessing.sharedctypes import RawArray
import numpy as np

buf = RawArray('d', 10)

def set_zero(i):
    data = np.frombuffer(buf)
    data[i] = 0

data = np.frombuffer(buf)
data[...] = np.arange(10)
p = multiprocessing.Pool(3)
p.map(set_zero, range(3))

print(data)
