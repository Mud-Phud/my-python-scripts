#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:02:27 2020

@author: robert

https://campus.datacamp.com/courses/introduction-to-data-visualization-in-python/customizing-plots?ex=1

Two data curves on same graph...

"""
import numpy as np
import matplotlib.pyplot as plt

# the data...
physical_sciences=np.array([13.8,14.9,14.8,16.5,18.2,19.1,20.,
21.3,22.5,23.7,24.6,25.7,27.3,27.6,
28.,27.5,28.4,30.4,29.7,31.3,
31.6,32.6,32.6,33.6,34.8,35.9,37.3,38.3,
39.7,40.2,41.,42.2,41.1,41.7,42.1,41.6,
40.8,40.7,40.7,40.7,40.2,40.1])
computer_science=np.array([13.6,13.6,14.9,16.4,18.9,19.8,23.9,25.7
,28.1,30.2,32.5,34.8,36.3,37.1
,36.8,35.7,34.7,32.4,30.8,29.9,29.4,28.7
,28.2,28.5,28.5,27.5,27.1,26.8
,27.,28.1,27.7,27.6,27.,25.1,22.2,20.6
,18.6,17.6,17.8,18.1,17.6,18.2])
year = np.array(range(1976,1976+42))

# Create a figure with 1x2 subplot and make the left subplot active
plt.subplot(1,2,1)

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Make the right subplot active in the current 1x2 subplot grid
plt.subplot(1,2,2)

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Use plt.tight_layout() to improve the spacing between subplots
plt.tight_layout()
plt.show()