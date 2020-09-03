#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:02:27 2020

@author: robert

https://campus.datacamp.com/courses/introduction-to-data-visualization-in-python/customizing-plots?ex=1

This code is deprecated

"""
import numpy as np
import matplotlib.pyplot as plt

# generate some data...

t = np.array(range(14))
temperature = t*6/14+27+np.random.normal(0,1,14) # linear growth in time plus random
dewpoint = 10*(35-temperature)**(-0.5)

plt.axes([0.05,0.05,0.425,0.9]) 
# Syntax: axes([x_lo,y_lo,width, height])  where the units are in "figure dimensions" between 0 and 1

plt.plot(t,temperature,'r')
plt.xlabel('Day')
plt.title('Temperature')



plt.axes([0.05,0.05,0.425,0.9])  # the following commands will be for this new plot
plt.plot(t,dewpoint,'b')
plt.xlabel('Day')
plt.title('Dewpoint')

plt.show()