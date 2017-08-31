from mpi4py import MPI
import numpy as np
from skimage import img_as_float, io
import matplotlib.pyplot as plt

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

img = img_as_float(io.imread('coffee.png', as_grey=True))
nrows, ncols = img.shape

img_part = img[:nrows//4, :].copy()*0
img_part_2 = img_part.copy()

comm.Scatter( [img, MPI.DOUBLE], [img_part, MPI.DOUBLE])

top_send = np.zeros(ncols, dtype=np.float64)
top_recv =  top_send.copy()
bottom_send = top_send.copy()
bottom_recv = top_send.copy()

t1 = MPI.Wtime()
for i in range(100):
    if rank > 0:
        top_send[...] = img_part[0, :]
        comm.Sendrecv(top_send, dest=rank-1, sendtag=10, recvbuf=top_recv, source=rank-1, recvtag=20)
        #comm.Isend(top_send, dest=rank-1, tag=10)
        #comm.Irecv(top_recv, source=rank-1, tag=20)
        
    if rank < size-1:
        bottom_send[...] = img_part[-1, :]
        comm.Sendrecv(bottom_send, dest=rank+1, sendtag=20, recvbuf=bottom_recv, source=rank+1, recvtag=10)
        #comm.Isend(bottom_send, dest=rank+1, tag=20)
        #comm.Irecv(bottom_recv, source=rank+1, tag=10)

    img_part_2[1:-1, 1:-1] =  (img_part[0:-2, 1:-1] + img_part[2:, 1:-1] +
        img_part[1:-1, 0:-2] + img_part[1:-1, 2:])/4.0

    comm.Barrier()

    if rank < size-1:
        img_part_2[-1, 1:-1] = (img_part[-2, 1:-1] + bottom_recv[1:-1] + img_part[-1, 0:-2] + img_part[-1, 2:])/4.0
    
    if rank > 0:
       img_part_2[0, 1:-1] = (img_part[1, 1:-1] + top_recv[1:-1] + img_part[0, 0:-2] + img_part[0, 2:])/4.0


    img_part_2, img_part = img_part, img_part_2
t2 = MPI.Wtime()

comm.Gather( [img_part, MPI.DOUBLE], [img, MPI.DOUBLE] )

if rank == 0:
    print(t2-t1)
    io.imshow(img)
    plt.show()

