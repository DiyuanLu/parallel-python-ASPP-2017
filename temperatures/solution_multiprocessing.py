import numpy as np
import h5py
import glob
import timeit
import matplotlib.pyplot as plt
import multiprocessing
import time

def make_plot(fname):
    data = np.loadtxt(fname, delimiter=",")
    plt.imshow(data)
    plt.savefig(fname.replace('.csv', '.png'))

plt.rcParams['image.cmap'] = 'plasma'

nfiles = len(glob.glob("*.csv"))
p = multiprocessing.Pool(4)
t1 = timeit.default_timer()
p.map(make_plot, glob.glob("*.csv"))
t2 = timeit.default_timer()


print(t2-t1)
