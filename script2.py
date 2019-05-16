# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:17:21 2019

@author: u5644101
"""
#my computer kept crashing when I ran the optical flow code, so I wrote this to extract the optical flow data.???
import xarray as xr
import numpy as np
ds = xr.open_dataset("C:/Users/u5644101/Downloads/sat_precip/sat_precip/H8_Flow.nc")
a = np.asarray(ds['B7'])
import pickle
out = open("FlowB7.pickle","wb")
pickle.dump(a, out)