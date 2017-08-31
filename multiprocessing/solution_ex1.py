import h5py
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool

data = h5py.File("weather.hdf5")
temps = data['temperature'][...]
years = range(2010, 2018)

def make_plot(i):
    print(i)
    plt.imshow(temps[i], interpolation='spline36')
    plt.savefig('{}.png'.format(years[i]))

p = Pool(1)
p.map(make_plot, range(8))
