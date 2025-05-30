import numpy as np
import xarray as xr

def chinamask_era5_global(ar,region=None):
    '''
    none: no mask
    choose region from: 'land','usaeast','china','europe','usa'
    '''
    if region==None:
        print('没mask')
        return ar
    
    sign = '-9999'
    if region=='land':
        with open(r'D:\lyt23\data\241026world\grid\era5_world_land_mask.txt', 'r') as f:
            array = [line.strip().split(' ') for line in f]
            arid = array[6:]
        for j in range(0, len(arid)):
            while '' in arid[j]:
                arid[j].remove('')
        arid=arid[::-1]
        for i in range(0,360):
            for j in range(0,1440):
                if arid[i][j] == sign:
                    ar[i][j] = np.nan
        print('world land mask')
        return ar
    if region=='usaeast':
        # with open(r'D:\lyt23\data\241026world\grid\usa_east_era5_mask.txt', 'r') as f:
        # with open(r'D:\lyt23\data\241026world\grid\e1.txt', 'r') as f:
        with open(r'D:\lyt23\data\241026world\grid\e22.txt', 'r') as f:
            array = [line.strip().split(' ') for line in f]
            arid = array[6:]
        for j in range(0, len(arid)):
            while '' in arid[j]:
                arid[j].remove('')
        arid=arid[::-1]
        for i in range(0,360):
            for j in range(0,1440):
                if arid[i][j] == sign:
                    ar[i][j] = np.nan
        print('usa east mask')
        return ar
    
    if region=='china':
        sign= '247'
    if region=='europe':
        sign='15444'
    if region=='usa':
        sign='444'

    # 读取mask id
    with open(r'D:\lyt23\data\241026world\grid\era5worldnorthneww.txt', 'r') as f:
    # with open(r'D:\lyt23\data\241026world\grid\new_worldera5north.txt', 'r') as f:
        array = [line.strip().split(' ') for line in f]
        arid = array[6:]
        for j in range(0, len(arid)):
            while '' in arid[j]:
                arid[j].remove('')
    arid=arid[::-1]
    for i in range(0,360):
        for j in range(0,1440):
            if arid[i][j] != sign:
                ar[i][j] = np.nan
    return ar


