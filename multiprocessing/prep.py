from skimage import io
import numpy as np
from skimage.transform import rescale
import glob
import h5py

data = np.loadtxt('2010.csv', delimiter=',')
data = rescale(data, 10)
nrows, ncols = data.shape

for filename in sorted(glob.glob('*csv'))[1:]:
    tmp = rescale(np.loadtxt(filename, delimiter=','), 10)
    print(tmp.shape)
    data = np.vstack([data, tmp])

data = data.reshape([-1, nrows, ncols])

# grow dataset exponentially:
for i in range(4):
    data = np.vstack([data, data])

f = h5py.File('weather.hdf5', 'w')
f.create_dataset("temperature", data=data)
