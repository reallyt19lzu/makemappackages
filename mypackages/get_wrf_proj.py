from __future__ import print_function
from wrf import getvar, interpline, CoordPair, xy_to_ll, ll_to_xy
from wrf import (to_np, getvar, smooth2d, get_cartopy, cartopy_xlim,
                 cartopy_ylim, latlon_coords)
from netCDF4 import Dataset
from wrf import getvar, ALL_TIMES

import netCDF4 as nc

def get_wrf_proj():
    ncfile = nc.Dataset(r"D:\lyt23\data\240326wrfout\old\2022072112_1\wrfout_d01_2022-07-23_14_00_00")
    lats, lons = latlon_coords(getvar(ncfile, "slp"))
    proj = get_cartopy(getvar(ncfile, "slp"))
    return proj, lats, lons
# %%
