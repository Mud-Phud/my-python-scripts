#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 04:59:25 2022

growing sine wave

see 

https://www.youtube.com/watch?v=F57_0XPdhD8
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Set up an empty fingure, axes, and line objects

fig, ax = plt.subplots()

# set axes limits so that the whole image is included

ax.set(xlim=(0,2*np.pi), ylim=(-1.1,1.1))

# Draw a blank line:

line, = ax.plot([],[])

# define data - one sine wave
x = np.linspace(0,2*np.pi,num=50)
y = np.sin(x)

# define the animate function

# Define animate function
def animate(i):
    line.set_data(x[:i], y[:i])
    return line,

# Define the animate(i) function. The integer i is the number
# of frames. Uses the line.set.data() method to draw the 
# first i elements of the sine curve for both x and y. 
# Note that you return line, with a comma again because
# you need to return an iterable and adding a comma 
# makes it a tuple. 

anim = FuncAnimation(fig,animate, frames = len(x)+1, interval = 30, blit=True)

# interval is the time that it waits
# frames needs to have 1 added for some reason
# blit = True

anim.save('sine.mp4')
