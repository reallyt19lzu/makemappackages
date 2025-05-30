
#%%
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
import matplotlib.ticker as mticker

from mypackages.lambert_ticks import *

#%% 南海子图、大地图
def make_nanhai_map(fig,proj1):

    # 南海子图
    ax_nh = fig.add_axes(
        [0.765, 0.110, 0.15, 0.2],
        projection=proj1
    )
    shape_path = r'C:\Users\user\Desktop\china1\zg\zg.shp'
    china = cfeature.ShapelyFeature(
        Reader(shape_path).geometries(),
        ccrs.PlateCarree(), edgecolor='k',
        facecolor='none')
    ax_nh.add_feature(china, lw=0.5, zorder=2)
    ax_nh.set_extent([105, 120, 0, 20], crs=ccrs.PlateCarree())

    return ax_nh


def make_map(ax, title, text):
    # proj = ccrs.PlateCarree()
    # fig = plt.figure(figsize=(30, 40), dpi=300)  # 创建页面
    shape_path = r'C:\Users\user\Desktop\china1\zg\zg.shp'
    china = cfeature.ShapelyFeature(
        Reader(shape_path).geometries(),
        ccrs.PlateCarree(), edgecolor='k',
        facecolor='none')
    # ax.grid(alpha=0.8,zorder=2)
    ax.add_feature(china, lw=0.5, zorder=2)
    # ax.add_feature(cfeature.LAND.with_scale('110m'),lw=1,color='white',zorder=2)
    # ax.add_feature(cfeature.OCEAN.with_scale('110m'),lw=1,color='white',zorder=2)
    # ax.add_feature(cfeature.COASTLINE.with_scale('110m'),lw=1,color='black',zorder=5)

    ax.set_extent([80, 130, 15, 55], crs=ccrs.PlateCarree())  # 设置范围

    # ax.set_xticks(range(70,140,20))
    #ax.set_xticklabels([str(x)+'°E' for x in range(70,140,20)],fontproperties = 'Arial',fontsize=11)
    # ax.set_yticks(range(15,50,15),crs=ccrs.PlateCarree())
    #ax.set_yticklabels([str(x)+'°N' for x in range(15,50,15)],fontproperties = 'Arial',fontsize=11)

    ax.tick_params(axis='both', labelsize=18)
    ax.set_title(title, fontproperties='Arial', fontsize=12, pad=4)
    #ax.text(70,57,text,fontsize=12,fontproperties = 'Arial')
    ax.set_aspect('auto')

    return ax

def gridlines(ax):
    xticks = [70, 80, 90, 100, 110, 120, 130, 140]
    yticks = [0, 10, 20, 30, 40, 50, 60]
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels={"bottom": "x", "left": "y"},
                        linewidth=0.5, color='gray', linestyle='--',
                        alpha=0.3,
                        x_inline=False, rotate_labels=False)
    gl.xlocator = mticker.FixedLocator(xticks)
    gl.ylocator = mticker.FixedLocator(yticks)
    gl.xformartter = LONGITUDE_FORMATTER
    gl.yformartter = LATITUDE_FORMATTER
    gl.xlabel_style = {'size': 13, 'color': 'k', 'font': 'Arial'}
    gl.ylabel_style = {'size': 13, 'color': 'k', 'font': 'Arial'}

    return xticks, yticks
# # %%
# from matplotlib import pyplot as plt
# ncfile = nc.Dataset(r"D:\lyt23\data\240326wrfout\old\2022072112_1\wrfout_d01_2022-07-23_14_00_00")
# lats, lons = latlon_coords(getvar(ncfile, "slp"))
# proj = get_cartopy(getvar(ncfile, "slp"))
# fig = plt.figure(figsize=(4, 3), dpi=300)  # 设置一个画板，将其返还给fig
# ax1 = fig.add_subplot(1, 1, 1, projection=proj)
# xticks, yticks = gridlines(ax1)
# # %%
# print(xticks)
