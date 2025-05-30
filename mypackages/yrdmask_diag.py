import numpy as np
import xarray as xr

#%%
def yrdmask_diag(ar):
    print('china=1，mask出yrd区域')
    # 读取中国id
    #上海310000，江苏320000，浙江330000，安徽340000
    with open(r'D:\lyt23\data\240326wrfout\provinceid.txt', 'r') as f:
        array = [line.strip().split(' ') for line in f]
        arid = array[6:]
        for j in range(0, len(arid)):
            while '' in arid[j]:
                arid[j].remove('')
    # mask过程    
    # ar.astype(float)       
    for i in range(0, 181):
        for j in range(0, 210):
            if (arid[i][j] != '310000') & (arid[i][j] != '320000') &\
            (arid[i][j] != '330000') & (arid[i][j] != '340000'):
                ar[i][j] = np.nan
    return ar