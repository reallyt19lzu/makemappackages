from __future__ import print_function
from wrf import getvar, interpline, CoordPair, xy_to_ll, ll_to_xy
from wrf import (to_np, getvar, smooth2d, get_cartopy, cartopy_xlim,
                 cartopy_ylim, latlon_coords)
from netCDF4 import Dataset
from wrf import getvar, ALL_TIMES

import netCDF4 as nc

def get_wrf_proj_world(region_sign=None):
    if region_sign is None:
        print('None: \nforgot to set region_sign, \nchose from china, europe, usa :)')
        return None, None, None
    else:
        path = 'D:\\lyt23\\data\\241026world\\geo\\geo_em.d01_'+region_sign+'.nc'
        ncfile = nc.Dataset(path)
        lats, lons = latlon_coords(getvar(ncfile, "HGT_M"))
        proj = get_cartopy(getvar(ncfile, "HGT_M"))
        return proj, lats, lons