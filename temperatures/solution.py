import numpy as np
import h5py
import glob
import timeit
import matplotlib.pyplot as plt

plt.rcParams['image.cmap'] = 'plasma'

t1 = timeit.default_timer()
nfiles = len(glob.glob("*.csv"))
for f in glob.glob("*.csv"):
    data = np.loadtxt(f, delimiter=",")
    plt.imshow(data)
    plt.savefig(f.replace('.csv', '.png'))
t2 = timeit.default_timer()
print(t2-t1)
