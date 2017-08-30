import numpy as np
from netCDF4 import Dataset
import glob

for nc_file in glob.glob("raw_data/*.nc"):
    fh = Dataset(nc_file, 'r')
    temps = fh.variables['air'][:]
    np.savetxt(nc_file.replace('.nc', '.csv'), temps[0], delimiter=',')
