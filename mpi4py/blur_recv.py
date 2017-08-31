from mpi4py import MPI
import numpy as np


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = np.ones(5, dtype = np.float64) * rank

data_send = data[:2].copy()
data_recv = np.zeros_like(data_send)

if rank == 0:
    comm.Sendrecv(data_send, dest=1, sendtag=10, recvbuf=data_recv, source=1, recvtag=20)
if rank == 1:
    comm.Sendrecv(data_send, dest=0, sendtag=20, recvbuf=data_recv, source=0, recvtag=10)

print(data_recv, rank)
