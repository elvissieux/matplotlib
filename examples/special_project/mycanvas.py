# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 09:07:51 2015

@author: François BAPTISTE
"""

import numpy as np  # NumPy (multidimensional arrays, linear algebra, ...)
import matplotlib as mpl         # Matplotlib (2D/3D plotting library)
import matplotlib.pyplot as plt  # Matplotlib's pyplot: MATLAB-like syntax

plt.figure("My visualiszation")

circle1=plt.Circle((0,0),.2,color='r')
circle2=plt.Circle((.5,.5),.2,color='b')
circle3=plt.Circle((1,1),.2,color='g',clip_on=False)
rect1 = matplotlib.patches.Rectangle( (-.25,.5), width=.5, height=1,color='c',alpha=.5)

fig = plt.gcf()
rect1.set_transform(fig.gca().transData+mpl.transforms.Affine2D().rotate_deg(-5))

fig.gca().add_artist(circle1)
fig.gca().add_artist(circle2)
fig.gca().add_artist(circle3)
fig.gca().add_artist(rect1)
fig.gca().axis("equal")
plt.xlim(-3,3)
plt.ylim(-1,5)