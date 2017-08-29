import numpy as np
import h5py
import glob
import timeit
import multiprocessing

#sums = []
#for f in glob.glob("*.csv"):
#    sums.append(np.sum(np.loadtxt(f, delimiter=',')))

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
    print(out.sum())

p = multiprocessing.Pool(4)
t1 = timeit.default_timer()
p.map(pairwise_distances, glob.glob("*.hdf5"))
t2 = timeit.default_timer()

print(t2-t1)
