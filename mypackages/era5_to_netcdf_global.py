'''
拼合era5计算获得的数据_global
'''
#%%
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
#%%
from mypackages.read_wrfout import *
#%%
# # 数据处理
import os
def era5_to_netcdf_global(fpath,fpathout=None,single_file=None):
    if single_file!=None:
        print('single_file')
        data_list = np.array(read_wrfout(fpath),dtype=float)[::-1]
        ds1 = xr.Dataset({'hin':(['year','lat','lon',],np.array(data_list,dtype=float).reshape(1,360,1440))},
                        coords= {
                                'lat':(['lat'],np.arange(0,90,0.25)),
                                'lon':(['lon'],np.arange(0,360,0.25)),
                                'year':(['year'],np.array([0]))
                                    }) 
        print(':)ok!')
        return ds1

    path=fpath

    def file_name(file_dir):
        files_path=[]
        files_name=[]
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1]=='.txt':
                    files_path.append(os.path.join(root,file))
                    files_name.append(os.path.splitext(file)[0])
        return files_path,files_name
    files_path1,files_name1=file_name(path)#读取数据
    files_path1

    data_list = []
    for i in range(len(files_path1)):
        print('read',i)
        data_list.append(np.array(read_wrfout(files_path1[i]),dtype=float)[::-1])
        # data_list.append(np.array(files_path1[i],dtype=float))

    ds1 = xr.Dataset({'hin':(['year','lat','lon',],np.array(np.array(data_list),dtype=float))},
                        coords= {
                                'lat':(['lat'],np.arange(0,90,0.25)),
                                'lon':(['lon'],np.arange(0,360,0.25)),
                                'year':(['year'],np.array(range(1960,2023+1)))
                                    }) 
    # 'check'
    plt.contourf(ds1.lon,ds1.lat,ds1.hin[:,:,:].mean(axis=0)[::-1])
    plt.colorbar()  
    print(':)ok!,but not saved, set fpathout!')
    if fpathout!=None:
        ds1.to_netcdf(fpathout)
        print(':)ok!,saved!')
    return
# %%
