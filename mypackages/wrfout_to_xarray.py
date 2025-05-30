import xarray as xr
import numpy as np
from wrf import to_np
def wrfout_to_xarray(ar,year,lats,lons):       
    ds1 = xr.Dataset({'hin': (['y', 'x', 'nyear'], np.array(ar, dtype=float).reshape(np.shape(lats)[0], np.shape(lats)[1], 1))},
                     coords={
        'lat': (['y', 'x'], to_np(lats)),
        'lon': (['y', 'x'], to_np(lons)),
        'year': (['year'], np.array([year]))
    },
        attrs=dict(
        description='variable_'+str(year)+'_variable_name',)
    )
    return ds1
'''def wrfout_to_xarray(ar,year,lats,lons):       
    ds1 = xr.Dataset({'hin': (['y', 'x', 'nyear'], np.array(ar, dtype=float).reshape(181, 210, 1))},
                     coords={
        'lat': (['y', 'x'], to_np(lats)),
        'lon': (['y', 'x'], to_np(lons)),
        'year': (['year'], np.array([year]))
    },
        attrs=dict(
        description='MaxO3_bio0_'+str(year)+'_variable_name',)
    )
    return ds1'''