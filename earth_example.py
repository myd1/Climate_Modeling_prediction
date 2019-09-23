import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# 运用 Basemap 函数我们可以在绘图区域中绘制地理信息相关的图像，当参数 projection 的值为 'ortho' #时，我们将得到一个如下所示的地球仪截面：

plt.figure(figsize=(8, 8))
m = Basemap(projection='ortho', resolution=None, lat_0=50, lon_0=-100)
m.bluemarble(scale=0.5)
plt.title("To see the world with you")
plt.savefig("earth.jpg",size = 13)
plt.show()
