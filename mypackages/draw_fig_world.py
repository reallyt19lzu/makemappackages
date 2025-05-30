from matplotlib import pyplot as plt
from mypackages.make_map_world import *
import cartopy.crs as ccrs

#%%

def draw_fig(proj,lon,lat,d,unit='unit',level=None,region=None,
             cmap='RdBu_r',title='title',pathout=None,transform_first=False,extend='both'):
    '''
    proj: get_wrf_proj
    '''
    if region==None:
        print('forgot region!!')
        return None
    if region=='china':
        fig = plt.figure(figsize=(8,3), dpi=500)  # 设置一个画板，将其返还给fig
        ax1 = fig.add_axes([0, 0.111, 0.25, 0.77],projection=proj)
        ax3p = [0.265, 0.15, 0.015, 0.7] #colorbar 位置
        ax1.text(150,20,'to control \n4:3 map font size',transform=ccrs.PlateCarree()) 
    else:
        fig = plt.figure(figsize=(4,3), dpi=500)  # 设置一个画板，将其返还给fig
        ax1 = fig.add_subplot(1, 1, 1, projection=proj)
        ax3p = [0.93, 0.15, 0.03, 0.7]

    ax1.set_global()
    make_map_world(ax1,title,'(a)',region)
    gridlines(ax1)
    # ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    fig.canvas.draw()
    lambert_xticks(ax1, gridlines(ax1)[0])
    lambert_yticks(ax1, gridlines(ax1)[1])
    # ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    c1 = ax1.contourf(#to_np(lons),to_np(lats),
                       lon,lat,
                       d,
                       extend=extend,levels=level,cmap=cmap,
                       transform=ccrs.PlateCarree(),
                       transform_first=transform_first)
    ax3 = fig.add_axes(ax3p)
    cb = fig.colorbar(c1, cax=ax3, shrink=0.01, extendrect=False, pad=0.03,)
                        # ticks=level)
    cb.ax.tick_params(axis='both', which='major', direction='out',
                        labelsize=11, length=4, width=0.5, labelfontfamily='Arial')
    cb.set_label(unit,
                    # rotation=270, 
                    labelpad=5, font='Arial', size=11)   
    
    if region=='china':
        c2 = make_nanhai_map_world(fig,proj).contourf(#to_np(lons),to_np(lats),
                                                    lon,lat,
                                                    (d),
                                                    cmap=cmap,extend='both',
                                                    # levels=np.arange(-3,3+0.5,0.5),
                                                    levels=level,
                                                    transform=ccrs.PlateCarree(),
                                                    transform_first=transform_first)
    if pathout != None:
        fig.savefig(pathout,
                    bbox_inches='tight')
    return fig