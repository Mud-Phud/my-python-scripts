#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 07:52:22 2020

@author: robert

All borrowed from 

https://pythonforundergradengineers.com/quiver-plot-with-matplotlib-and-jupyter-notebooks.html


"""

import numpy as np
import matplotlib.pyplot as plt

# first let's look at numpy's meshgrid method...

a = np.array([1,2,3])
b = np.array([-1,0,1])

a_1, b_1 = np.meshgrid(a,b)

print(a_1); print(b_1)

for i in range(3):
    for j in range(3):
        print(a_1[i,j],b_1[i,j])

# Thus the mesh grid is used to run over all possible combinations from 
# the two sets a and b. 
        
# Ok. Here is a boring quiver plot with just one vector:
        

fig, ax = plt.subplots()

x_pos = 0
y_pos = 0
x_direct = 1
y_direct = 1

ax.quiver(x_pos,y_pos,x_direct,y_direct)

plt.show()

# a little less boring quiver plot with two vectors...

fig, ax = plt.subplots()

x_pos = [0, -0.5]
y_pos = [0, 0.5]
x_direct = [1, 0]
y_direct = [1, -1]

ax.quiver(x_pos,y_pos,x_direct,y_direct, scale=5)
ax.axis([-1.5,1.5,-1.5,1.5])

plt.title("Quiver Plot with two vectors")

plt.show()

# Note that the vectors were scaled up by a factor of 5

# Finally, let's get something more interesting. We use the meshgrid method.

x = np.arange(0,2.2,0.2)
y = np.arange(0,2.2,0.2)

X, Y = np.meshgrid(x, y)
u = np.cos(X)*Y
v = np.sin(y)*Y

fig, ax = plt.subplots(figsize=(7,7))
ax.quiver(X,Y,u,v)

#ax.xaxis.set_ticks([])  # removes the ticks from the x-axis
#ax.yaxis.set_ticks([])  # ditto for the y-axis
ax.axis([-0.2, 2.3, -0.2, 2.3])
ax.set_aspect('equal')  # makes sure the aspect ration is 1:1

plt.show()

# here's another....

x = np.arange(-5,6,1)
y = np.arange(-5,6,1)

X, Y = np.meshgrid(x, y)

u, v = X/5, -Y/5

fig, ax = plt.subplots(figsize=(7,7))
ax.quiver(X,Y,u,v)

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.axis([-6, 6, -6, 6])
ax.set_aspect('equal')

plt.show()

# Try one with a gradient...

x = np.arange(-2,2.2,0.2)
y = np.arange(-2,2.2,0.2)

X, Y = np.meshgrid(x, y)
z = X*np.exp(-X**2 -Y**2)
dx, dy = np.gradient(z)

fig, ax = plt.subplots(figsize=(7,7))
ax.quiver(X,Y,dx,dy)

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.set_aspect('equal')

plt.show()

# another gradient with simple repeller...

x = np.arange(-2.001,2.2,0.2)
y = np.arange(-2.001,2.2,0.2)

X, Y = np.meshgrid(x, y)
z = X**2 + Y**2
dx, dy = np.gradient(z)

fig, ax = plt.subplots(figsize=(7,7))
ax.quiver(X,Y,dx,dy)

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.set_aspect('equal')

plt.show()

# Here is one with vortices...
#
# The equation is \vec{F} = sin(x)cos(y) \ \hat{i} -cos(x)sin(y) \ \hat{j}


x = np.arange(0,2*np.pi+2*np.pi/20,2*np.pi/20)
y = np.arange(0,2*np.pi+2*np.pi/20,2*np.pi/20)

X,Y = np.meshgrid(x,y)

u = np.sin(X)*np.cos(Y)
v = -np.cos(X)*np.sin(Y)

fig, ax = plt.subplots(figsize=(7,7))

ax.quiver(X,Y,u,v)

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.axis([0,2*np.pi,0,2*np.pi])
ax.set_aspect('equal')

plt.show()

