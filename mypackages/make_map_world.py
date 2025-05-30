
#%%
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
import matplotlib.ticker as mticker

from mypackages.lambert_ticks import *

#%% 南海子图、大地图
def make_nanhai_map_world(fig,proj1):

    # 南海子图
    ax_nh = fig.add_axes(
        [0.108, 0.111, 0.22, 0.21],
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


def make_map_world(ax, title, text,region):
    # 具体的extent还得等wrfout出来之后重新处理
    # proj = ccrs.PlateCarree()
    # fig = plt.figure(figsize=(30, 40), dpi=300)  # 创建页面
    if region=='china':
        shape_path = r'C:\Users\user\Desktop\china1\zg\zg.shp'
        # shape_path = r'C:\Users\user\Desktop\china1\world\ne_10m_admin_1_states_provinces.shp'
        shape = cfeature.ShapelyFeature(
            Reader(shape_path).geometries(),
            ccrs.PlateCarree(), edgecolor='k',
            facecolor='none')
        ax.set_extent([103, 130, 16, 55], crs=ccrs.PlateCarree())

    if region=='usa':
        shape_path = r'C:\Users\user\Desktop\china1\usa\usa.shp'
        shape = cfeature.ShapelyFeature(
            Reader(shape_path).geometries(),
            ccrs.PlateCarree(), edgecolor='k',
            facecolor='none')
        ax.set_extent([-120, -70, 25, 51], crs=ccrs.PlateCarree())  # usa
    if region=='europe':
        shape_path = r'C:\Users\user\Desktop\china1\europe\europe.shp'
        shape = cfeature.ShapelyFeature(
            Reader(shape_path).geometries(),
            ccrs.PlateCarree(), edgecolor='k',
            facecolor='none')
        ax.set_extent([-12, 35, 35, 63], crs=ccrs.PlateCarree())  # euro
    # ax.grid(alpha=0.8,zorder=2)
    ax.add_feature(shape,lw=0.5,zorder=2)
    # ax.add_feature(cfeature.BORDERS.with_scale('110m'), lw=0.5, zorder=2)
    # ax.add_feature(cfeature.LAND.with_scale('110m'),lw=1,color='white',zorder=2)
    # ax.add_feature(cfeature.OCEAN.with_scale('110m'),lw=1,color='white',zorder=2)
    # ax.add_feature(cfeature.COASTLINE.with_scale('110m'),lw=1,color='black',zorder=5)

    # ax.set_xticks(range(70,140,20))
    #ax.set_xticklabels([str(x)+'°E' for x in range(70,140,20)],fontproperties = 'Arial',fontsize=11)
    # ax.set_yticks(range(15,50,15),crs=ccrs.PlateCarree())
    #ax.set_yticklabels([str(x)+'°N' for x in range(15,50,15)],fontproperties = 'Arial',fontsize=11)

    ax.tick_params(axis='both', labelsize=18)
    ax.set_title(title, fontproperties='Arial', fontsize=12, pad=15)
    #ax.text(70,57,text,fontsize=12,fontproperties = 'Arial')
    ax.set_aspect('auto')

    return ax

def gridlines(ax):
    xticks = [-180,-170,-160,-150,-140,-130,-120,-110,-100,
              -90,-80,-70,-60,-50,-40,-30,-20,-10,0,
              10,20,30,40,50,60,
              70, 80, 90, 100, 110, 120, 130, 140]
    # yticks = [0, 10, 20, 30, 40, 50, 60]
    yticks = [0, 15, 25, 35, 45, 55, 65]
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels={"bottom": "x", "left": "y"},
                        linewidth=0.5, color='gray', linestyle='--',
                        alpha=0, #0.3
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
