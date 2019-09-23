import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


#将参数projection的值设置为'lcc'时，我们可以通过经纬度设置来得到某一区域的局部地图：

fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution=None,
            width=8E6, height=8E6,
            lat_0=45, lon_0=-100, )
m.etopo(scale=0.5, alpha=0.5)

# 将经纬度映射为 (x, y) 坐标，用于绘制图像
x, y = m(-122.3, 47.6) #改变经纬度获取需要标记的城市
plt.plot(x, y, 'ok', markersize=5)
plt.text(x, y, ' Seattle', fontsize=12)
plt.savefig("save.png")
plt.show()