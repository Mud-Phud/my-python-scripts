#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:21:08 2020

@author: robert
"""
import numpy as np

f = np.array([1, 2, 4, 7, 11, 16], dtype=float)
print(np.gradient(f))

print(np.gradient(f, 2))

x = np.arange(f.size)
print(x)
print(np.gradient(f, x))

x = np.array([0., 1., 1.5, 3.5, 4., 6.], dtype=float)
print(x)
print(np.gradient(f, x))

y=np.array([[1,3,2,6],[4,5,3,8],[12,10,7,4],[1,2,4,7]],dtype=float)
print(np.gradient(y))


x = np.array([[2.5,3.5,6.5,8.5],[8,7,5,2],[3,4.2,6,4],[3,8,9,])

y = np.array([5, 7, 4, 8])
print(np.gradient(y,0.5))
print(np.gradient(y, np.array([0,1,3,3.5])))


def f(x, y):
    return x*x-y*y

x=np.array([1.5,2.5,3.5])
y=np.array([1.0,2.0,3.0])

X,Y = np.meshgrid(x,y)

print(X)
print(Y)

Z=f(X,Y)

#ax = plt.axes(projection='3d')
fig = plt.figure()

ax.scatter3D(X, Y, Z, cmap='Greens')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');

plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

day = np.array([0,1,2,3,4])
time = np.array([9.5,12.0,14.5,17.0])

Day,Time = np.meshgrid(day, time)
    
data = np.array([
        [2,3,1,3,4],
        [4,3,4,6,5],
        [6,7,8,10,9],
        [3,4,6,7,8]
        ])


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(Day, Time, data, color='black')
ax.set_title('wireframe')
plt.show()

np.gradient(data)

x=np.array([0.6,0.9,1.2,1.5])
y=np.array([0.36,.81,1.44, 2.25])

print(np.gradient(y,0.3))

x=np.array([0.6,0.9,1.4,1.5])
y=np.array([0.36,.81,1.96,2.25])
print(np.gradient(y,x))