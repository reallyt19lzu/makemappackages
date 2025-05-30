import numpy as np
import xarray as xr

def chinamask_era5(ar):
    print('china=1，mask出中国区域')
    # 读取中国id
    with open(r'F:\240912\hwcharacter\provinceidera5.txt', 'r') as f:
        array = [line.strip().split(' ') for line in f]
        arid = array[6:]
        for j in range(0, len(arid)):
            while '' in arid[j]:
                arid[j].remove('')
    # mask过程    
    # ar.astype(float)       
    for i in range(0, 240):
        for j in range(0, 280):
            if arid[i][j] == '-9999':
                ar[i][j] = np.nan
    return ar

# def chinamask_era5(ar):
#     print('china=1，mask出中国区域')
#     # 读取中国id
#     with open(r'F:\240912\hwcharacter\newch.txt', 'r') as f:
#         array = [line.strip().split(' ') for line in f]
#         arid = array[6:]
#         for j in range(0, len(arid)):
#             while '' in arid[j]:
#                 arid[j].remove('')
#     # mask过程    
#     # ar.astype(float)       
#     for i in range(0, 240):
#         for j in range(0, 280):
#             if arid[i][j] != '2752514':
#                 ar[i][j] = np.nan
#     return ar
