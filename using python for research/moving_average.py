#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 17:43:41 2018

@author: robert

Excercise 3a


    Write a function moving_window_average(x, n_neighbors) that takes a list x and the number of neighbors n_neighbors on either side of a given member of the list to consider.
    For each value in x, moving_window_average(x, n_neighbors) computes the average of that value's neighbors, where neighbors includes the value itself.
    moving_window_average should return a list of averaged values that is the same length as the original list.
    If there are not enough neighbors (for cases near the edge), substitute the original value as many times as there are missing neighbors.
    Use your function to find the moving window sum of x=[0,10,5,3,1,5] and n_neighbors=1.

"""
x=[0,10,5,3,1,5]

"""
first we pad x with the first entry repeated n_neighbors times
and the last entry repeated n_neighbors times. 

Say, if n_neighbors = 2, then x is padded on both sides to

[0, 0, 0, 10, 5, 3, 1, 5, 5, 5]

now the moving average vector at 0 will be the average of x[0],
x[1], x[2] (which is the original x[0]), x[3], and x[4]. 

The moving average vector at 1 will be the average of x[1],
x[2], x[3] (which is the original x[1]), x[4], and x[5] and so 
forth.
"""

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    # we "pad" the vector x on each side...
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    mwa = [0] * n # we put place holders in the vector
    for i in range(n):
        mwa[i] = sum(x[j+n_neighbors+i] for j in range(-n_neighbors,n_neighbors+1))/width
    return mwa

#%%

import random

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.
R = 1000
x=[random.uniform(0,1) for i in range(R)]

Y =[[x[i] for i in range(R)]]

#%%

for j in range(1,10):
    xmvaj = moving_window_average(x,j)
    Y.append(xmvaj)

#%%
    
    
ranges = [max(Y[i])-min(Y[i]) for i in range(10)]
print(ranges)

        