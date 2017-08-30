import numpy as np
from skimage import io
from skimage.transform import rescale
import glob
import os

scale = 1

for f in glob.glob("raw_data/*.csv"):
    data = np.loadtxt(f, delimiter=',')
    data_scaled = rescale(data, scale)
    print(os.path.basename(f))
    np.savetxt(os.path.basename(f), data_scaled, delimiter=',')
