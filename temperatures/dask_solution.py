import dask
import dask.array as da
import glob
import h5py
import timeit

dsets = [da.from_array(h5py.File(f)['temperature'], chunks=(1169, 2500)) for f in glob.glob("*.hdf5")]
temperatures = da.stack(dsets)

t1 = timeit.default_timer()
print(temperatures.mean().compute())
t2 = timeit.default_timer()
print(t2-t1)
