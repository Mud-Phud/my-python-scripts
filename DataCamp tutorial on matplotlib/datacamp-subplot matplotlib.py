#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 23:59:03 2020

@author: robert

DataCamp using subplot()
"""
import numpy as np
import matplotlib.pyplot as plt

# generate some data...

t = np.array(range(14))
temperature = t*6/14+27+np.random.normal(0,1,14) # linear growth in time plus random
dewpoint = 10*(35-temperature)**(-0.5)

plt.subplot(2,1,1)

plt.plot(t,temperature,'r')
plt.xlabel('Day')
plt.title('Temperature')

plt.subplot(2,1,2)
plt.plot(t,dewpoint,'b')
plt.xlabel('Day')
plt.title('Dewpoint')

plt.tight_layout()

plt.show()