#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 07:11:06 2020

@author: robert

matplotlib with equal axis vs not
"""
import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(0,2*(np.pi+0.1),0.1)
x = np.cos(theta)
y = np.sin(theta)

plt.subplot(2,1,1)
plt.plot(x,y,'red')
plt.title('default axis')
plt.subplot(2,1,2)
plt.plot(x,y,'red')
plt.axis('equal')
plt.title('axis equal')
plt.tight_layout()
plt.show()

