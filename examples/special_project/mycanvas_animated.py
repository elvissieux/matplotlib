# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 09:07:51 2015

@author: François BAPTISTE
"""

import numpy as np  # NumPy (multidimensional arrays, linear algebra, ...)
import matplotlib as mpl         # Matplotlib (2D/3D plotting library)
import matplotlib.pyplot as plt  # Matplotlib's pyplot: MATLAB-like syntax

from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.gridspec as gridspec


fig = plt.figure("My visualization")

gs1 = gridspec.GridSpec(2, 1, width_ratios=[1],height_ratios=[10,1])
ax1 = fig.add_subplot(gs1[0])
ax2 = fig.add_subplot(gs1[1])

circle1=plt.Circle((0,0),.2,color='r')
circle2=plt.Circle((.5,.5),.2,color='b')
circle3=plt.Circle((1,1),.2,color='g',clip_on=False)
rect1 = mpl.patches.Rectangle( (-.25,.5), width=.5, height=1,color='c',alpha=.5)


rect1.set_transform(ax1.transData+mpl.transforms.Affine2D().rotate_deg(-5))

ax1.add_artist(circle1)
ax1.add_artist(circle2)
ax1.add_artist(circle3)
ax1.add_artist(rect1)
ax1.axis("equal")
ax1.set_xlim(-3,3)
ax1.set_ylim(-1,5)

sfreq = Slider(ax2, 'Freq', 0, 90.0, valinit=0.)

fig.tight_layout()

def update(val):
    rect1.set_transform(ax1.transData+mpl.transforms.Affine2D().rotate_deg(sfreq.val))
    ax1.draw()
sfreq.on_changed(update)