#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plotting a parabola!
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,1.7,0.1)
y = x*x

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot([0.6,0.9,1.2],[0.36,.81,1.44],'ro')

ax.set_aspect('equal')
plt.show()


# on the same row...



f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.plot([0.6,0.9,1.2,1.5],[0.36,.81,1.44, 2.25],'ro')

ax2.plot(x, y)
ax2.plot([0.6,0.9,1.4,1.5],[0.36,.81,1.96,2.25],'ro')
plt.show()