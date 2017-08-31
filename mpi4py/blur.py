from mpi4py import MPI
import numpy as np
from skimage import data, io

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print("Hello, I am a process {} out of {}".format(rank, size))

img = data.load('coffee.png', as_grey=True)
nrows, ncols = img.shape
img_chunk = np.zeros([nrows//4, ncols], dtype = np.float64)
print(img_chunk.shape)

comm.Scatter([img, MPI.DOUBLE], [img_chunk, MPI.DOUBLE])# Scatter(target, result)
#io.imshow(img_chunk)
#io.show()

#for i in range(1, size)

nrows, ncols = img_chunk.shape
img_chunk_copy = img_chunk.copy()
for i in range(100):
    img_chunk_copy[1: -1, 1:-1] = (img_chunk[2:, 1:-1] + img_chunk[0:-2, 1:-1]+img_chunk[1:-1:,0:-2 ]+img_chunk[1:-1, 2:])/4.0

    img_chunk, img_chunk_copy = img_chunk_copy, img_chunk
