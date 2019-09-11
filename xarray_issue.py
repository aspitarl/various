# Your code here
import numpy as np
import xarray as xr
import pandas as pd
import time

size = 1000000
data = np.random.random(size)
times = pd.date_range('2019-01-01', periods=size, freq='ms')
da = xr.DataArray(data, dims=['time'], coords={'time': times})

start = time.time()

da.resample(time='s').mean()

print('Elapsed time: ' + str(time.time() - start))
print('xarray version: ' + str(xr.__version__))
