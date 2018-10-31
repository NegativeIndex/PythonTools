
#
#import matplotlib.pyplot as plt
#import matplotlib.cbook as cbook
#from matplotlib_scalebar.scalebar import ScaleBar
#plt.figure()
#image = plt.imread('Sample1/Image71.TIF')
#fig=plt.imshow(image)
##scalebar = ScaleBar(0.128,units='um',
##                    color='w',box_alpha=0.,
##                    location='upper left') # 1 pixel = 0.2 meter
##plt.gca().add_artist(scalebar)
##
#plt.axis('off')
#fig.axes.get_xaxis().set_visible(False)
#fig.axes.get_yaxis().set_visible(False)
#plt.savefig("test.png", bbox_inches='tight', pad_inches = 0)
#plt.show()


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib_scalebar.scalebar import ScaleBar
import numpy as np
  

infile='S1 metal/Image97.TIF'
outfile='Image97.TIF'

data = mpimg.imread(infile)
shape=np.shape(data)[0:2][::-1]
dpi=300
size = [float(i)/dpi for i in shape]

fig = plt.figure()
fig.set_size_inches(size)
ax=plt.Axes(fig,[0,0,1,1])
ax.set_axis_off()
fig.add_axes(ax)
scalebar = ScaleBar(1.333,units='um',
                color='w',box_alpha=0.,
                location='lower left') # 1 pixel = 0.2 meter
plt.gca().add_artist(scalebar)
ax.imshow(data)
fig.savefig('Image97_1.png', dpi=dpi)
plt.show()
