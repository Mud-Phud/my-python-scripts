#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 21:33:27 2020

@author: robert

Graphs level lines of complex functions. Suppose f(z) is a complex function.
We want to graph the images of the level lines x_0+i y and x+i y_0.
"""
import numpy as np
import matplotlib.pyplot as plt

def f(z):
    return -1/z

def u(x,y):
    return -x/(x**2+y**2)**(0.5)

def v(x,y):
    return y/(x**2+y**2)**(0.5)

x0 = 0.5
y = np.arange(0.1,2.1,0.1)
x = np.ones(len(y))*x0

U = np.array([u(x[i],y[i]) for i in range(len(y))])
V = np.array([v(x[i],y[i]) for i in range(len(y))])
#
#fig,a =  plt.subplots(2,0)
#a[0][0].plot(x,y)
#a[1][0].plot(U.V)

fig, (ax1, ax2) = plt.subplots(1, 2,sharey=True)
ax1.plot(x, y)

ax2.plot(U,V)

plt.show()