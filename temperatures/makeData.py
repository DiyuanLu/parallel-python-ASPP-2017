import datetime
from skimage import io, img_as_float
from skimage.transform import rescale
import numpy as np
import matplotlib.pyplot as plt
import sys
import h5py

start_date = datetime.date(2017, 1, 1)
days = 20
min_temp = -80.
max_temp = 50.
scale = 1

try:
    write_hdf5 = sys.argv[1]
except IndexError:
    write_hdf5 = False

img = img_as_float(io.imread('template.jpg', as_grey=True))
img = min_temp + img*(max_temp - min_temp)
img = rescale(img, scale)
img = img[:15, :15]
ny, nx = img.shape


for day in range(days):
    date = str(start_date + datetime.timedelta(days=day))
    noise = np.random.rand(ny, nx)*(max_temp - min_temp)/10

    if write_hdf5:
        filename = date+'.hdf5'
        f = h5py.File(filename)
        f.create_dataset('temperature', data=img+noise)
    else:
        filename = date+'.csv'
        np.savetxt(filename, img+noise, delimiter=',')
    print("Wrote {}".format(filename))
