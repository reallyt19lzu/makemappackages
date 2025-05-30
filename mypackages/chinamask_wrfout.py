import numpy as np
import xarray as xr

#%%
def chinamask_wrfout(ar,diag=0):
    print('china=1，mask出中国区域')
    # 读取中国id
    with open(r'D:\lyt23\data\240326wrfout\provinceid.txt', 'r') as f:
        array = [line.strip().split(' ') for line in f]
        arid = array[6:]
        for j in range(0, len(arid)):
            while '' in arid[j]:
                arid[j].remove('')
    if diag==1:
        arid=arid[::-1]
    # mask过程    
    # ar.astype(float)       
    for i in range(0, 181):
        for j in range(0, 210):
            if arid[i][j] == '-9999':
                ar[i][j] = np.nan
    return ar

