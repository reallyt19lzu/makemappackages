import numpy as np
import xarray as xr

#%%
def mask_wrfout_global(ar,region=None,diag=0):
    '''
    china,europe,usa
    yrd,scb,europewest,northeastusa
    '''
    if region==None:
        print('没mask')
        return ar
    if region=='china':
        print('region=china')
        idpath ='D:\\lyt23\\data\\241026world\\grid\\wrf_mask_china.txt'
    if region=='europe':
        print('region=europe')
        idpath ='D:\\lyt23\\data\\241026world\\grid\\wrf_mask_euro.txt'
    if region=='usa':
        print('region=usa')
        idpath ='D:\\lyt23\\data\\241026world\\grid\\wrf_mask_usa.txt'
    if region=='yrd':
        print('region=yrd')
        idpath ='D:\\lyt23\\data\\241026world\\grid\\wrf\\mask\\wrf_mask_yrd.txt'
    if region=='scb':
        print('region=scb')
        idpath ='D:\\lyt23\\data\\241026world\\grid\\wrf\\mask\\wrf_mask_scb.txt'
    if region=='europecenter':
        print('region=europecenter')
        idpath ='D:\\lyt23\\data\\241026world\\grid\\wrf\\mask\\wrf_mask_europecenter.txt'
    if region=='eastusa':
        print('region=eastusa')
        idpath ='D:\\lyt23\\data\\241026world\\grid\\wrf\\mask\\wrf_mask_eastusa.txt'
    if region=='europewest':
        print('region=europewest')
        idpath ='D:\\lyt23\\data\\241026world\\grid\\wrf\\mask\\wrf_mask_europewest.txt'
    if region=='northeastusa':
        print('region=northeastusa')
        idpath ='D:\\lyt23\\data\\241026world\\grid\\wrf\\mask\\wrf_mask_northeastusa.txt'

    if region=='bvocnortheastusa':
        print('region=bvocnortheastusa')
        idpath ='D:\\lyt23\\data\\241026world\\grid\\wrf\\mask\\bvoc-northeastusa.txt'
    if region=='bvoceuropewest':
        print('region=bvoceuropewest')
        # idpath ='D:\\lyt23\\data\\241026world\\grid\\wrf\\mask\\bvoc-europewestnew.txt'
        # idpath ='D:\\lyt23\\data\\241026world\\grid\\wrf\\mask\\bvoc-europewest.txt'
        idpath ='D:\\lyt23\\data\\241026world\\grid\\wrf\\mask\\bvoc-europewestnew1.txt'
    if region=='bvoceuropecenter':
        print('region=bvoceuropecenter')
        idpath ='D:\\lyt23\\data\\241026world\\grid\\wrf\\mask\\bvoc-europecenter.txt'
    if region=='bvocyrd':
        print('region=bvocyrd')
        idpath ='D:\\lyt23\\data\\241026world\\grid\\wrf\\mask\\bvoc-yrd.txt'
    # 读取中国id
    with open(idpath, 'r') as f:
        array = [line.strip().split(' ') for line in f]
        arid = array[6:]
        for j in range(0, len(arid)):
            while '' in arid[j]:
                arid[j].remove('')
    if diag==1:
        arid=arid[::-1]
    # mask过程    
    # ar.astype(float)       
    for i in range(0, np.shape(arid)[0]):
        for j in range(0, np.shape(arid)[1]):
            if arid[i][j] == '-9999':
                ar[i][j] = np.nan
    return ar
