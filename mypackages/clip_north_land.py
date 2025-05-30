import cartopy.io.shapereader as shpreader
from cartopy.mpl.patch import geos_to_path
from matplotlib.path import Path
def clip_north_land(ax):
    # 读取shp文件
    shp_path = r'C:\Users\user\Desktop\china1\world\north.shp'
    shp = shpreader.Reader(shp_path)
    geo_list = list(shp.geometries())
    poly = geo_list[:]
    path = Path.make_compound_path(*geos_to_path(poly))
    # 白化中国以外的区域
    for col in ax.collections:
        col.set_clip_path(path, transform=ax.transData)