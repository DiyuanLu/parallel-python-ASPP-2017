import multiprocessing
from multiprocessing.sharedctypes import RawArray
from ctypes import c_double
import numpy as np

data = np.arange(10)
print(data)

def set_zero(i):
    data[i] = 0

p = multiprocessing.Pool(3)
p.map(set_zero, range(3))

print(data)
