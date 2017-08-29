import numpy as np
import h5py
import glob
import timeit

nfiles = len(glob.glob("*.hdf5"))


def distance(x1, x2):
    return np.abs(x2 - x1)

def pairwise_distances(fname):
    h5f = h5py.File(fname, 'r')
    temps = h5f['temperature']
    ny, nx = temps.shape
    out = np.zeros_like(temps)*0.0

    for i in range(ny):
        for j in range(nx):
            distance_sum = 0
            tmp = temps[i, j]
            for i_1 in range(ny):
                for j_1 in range(nx):
                    distance_sum += distance(tmp, temps[i_1, j_1])
            out[i, j] = distance_sum
    return out.sum()

t1 = timeit.default_timer()
sums = []
for f in glob.glob("*.hdf5"):
    print(f)
    print(pairwise_distances(f))
t2 = timeit.default_timer()

print(t2-t1)
