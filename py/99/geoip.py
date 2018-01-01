import requests
import json
from urllib import request
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib import style

my_ip = json.loads(requests.get("http://ip.jsontest.com/").text)["ip"]
print (my_ip)

geoip_url = "http://www.freegeoip.net/json/" + my_ip
geoip_data = requests.get(geoip_url).text
geoip = json.loads(geoip_data)
print(json.dumps(geoip, indent=4, sort_keys=True))

#mpl.style.use('map')
fig = plt.figure(figsize=(22, 12))
#X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
#C,S = np.cos(X), np.sin(X)

#plt.plot(X,C)
#plt.plot(X,S)
ax = fig.add_subplot(111, axisbg='w', frame_on=False)
fig.suptitle('HI', fontsize=30, y=.95)

m = Basemap(lon_0=0, projection='robin')
m.drawmapboundary(color='w')

shapefile = "ne_10m_admin_0_countries"
m.readshapefile(shapefile, 'units', color='#444444', linewidth=.2)

ax = fig.add_subplot(111, axisbg='w', frame_on=False)
ax.axhspan(0, 1000 * 1800, facecolor='w', edgecolor='w', zorder=2)

ax_legend = fig.add_axes([0.35, 0.14, 0.3, 0.03], zorder=3)
#cmap = mpl.colors.ListedColormap(scheme)
#cb = mpl.colorbar.ColorbarBase(ax_legend, cmap=cmap, ticks=bins, boundaries=bins, orientation='horizontal')
#cb.ax.set_xticklabels([str(round(i, 1)) for i in bins])
#plt.annotate(descripton, xy=(-.8, -3.2), size=14, xycoords='axes fraction')

plt.show()
fig.show()
