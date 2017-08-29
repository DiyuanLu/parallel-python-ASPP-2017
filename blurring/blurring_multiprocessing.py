from skimage import data, io
from skimage.transform import rescale
import matplotlib.pyplot as plt
import numpy as np

import multiprocessing
import multiprocessing.sharedctypes
import ctypes

import functools
import itertools

scale = 2

img = rescale(data.load('coffee.png', as_grey=True), scale)
nrows, ncols = img.shape

shared_array_1 = multiprocessing.sharedctypes.RawArray(ctypes.c_double, nrows*ncols)
shared_array_2 = multiprocessing.sharedctypes.RawArray(ctypes.c_double, nrows*ncols)

def blur(rows, flip, start_row, in_ary=shared_array_1, out_ary=shared_array_2):

    if flip:
        in_data = np.frombuffer(in_ary).reshape([nrows, ncols])
        out_data = np.frombuffer(out_ary).reshape([nrows, ncols])
    else:
        out_data = np.frombuffer(in_ary).reshape([nrows, ncols])
        in_data = np.frombuffer(out_ary).reshape([nrows, ncols])

    ny, nx = in_data.shape
    
    tile_start = start_row
    tile_end = start_row+rows
    
    if tile_start == 0:
        tile_start = tile_start+1
    if tile_end == ny:
        tile_end = tile_end-1

    for i in range(tile_start, tile_end):
        for j in range(1, nx-1):
            out_data[i, j] = (in_data[i, j-1] + in_data[i, j+1] + 
                                    in_data[i-1, j] + in_data[i+1, j])/4.0

n = 50
nprocs = 4

img = np.frombuffer(shared_array_1).reshape([nrows, ncols])
img_cpy = np.frombuffer(shared_array_2).reshape([nrows, ncols])

img[...] = rescale(data.load('coffee.png', as_grey=True), scale)
img_cpy[...] = img[...]

p = multiprocessing.Pool(nprocs)

import timeit

t1 = timeit.default_timer()
for step, flip in zip(range(n), itertools.cycle([0, 1])):
    wrapped_blur = functools.partial(blur, nrows//nprocs, flip)
    p.map(wrapped_blur, range(0, nrows, nrows//nprocs))
t2 = timeit.default_timer()
print("Time took: ", t2-t1)

io.imshow(img)
plt.show() 
