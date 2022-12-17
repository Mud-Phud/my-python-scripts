#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 17:06:36 2022

@author: robert

An interesting integral based function.

tau(s) = int(0,infinity, x**(s-1)/(exp(x)-1) )

"""
import numpy as np


def integrand(s,t):
    return t**(s-1)/(np.exp(t)-1)

def tau(s):

    a=0.05;b=15;n=101
    h = (b-a)/(n-1)
    t = np.linspace(a,b,n) 
    y = integrand(s,t)
    return (h/3)*(2*sum(y[::2])-y[0]-y[-1] + 4*sum(y[1::2]))

s = np.linspace(.1,5,100)
y = []
for s_i in s:
    y.append(tau(s_i))

    

import matplotlib.pyplot as plt
plt.plot(s,y)
plt.ylabel('$\int\limits _{0}^{\infty}\frac{x^{s-1}}{e^{x}-1}d$')
plt.show()

import matplotlib.pyplot as plt

x1 = np.linspace(0.2,5, 100)
s1 = 1.2
y1 = x**(s1-1)/(np.exp(x)-1)

x2 = np.linspace(0.1,5, 100)
s2 = 2
y2 = x**(s2-1)/(np.exp(x)-1)

x3 = np.linspace(0.001,5, 100)
s3 = 2.5
y3 = x**(s3-1)/(np.exp(x)-1)

x4 = np.linspace(0.01,5, 100)
s4 = 1.8
y4 = x**(s4-1)/(np.exp(x)-1)

  
# Plotting  the curves simultaneously
plt.plot(x1, y1, color='r', label='s=1.2')
plt.plot(x2, y2, color='g', label='s=2')
plt.plot(x3, y3, color='b', label='s=2.5')
plt.plot(x4, y4, color='c', label='s=1.8')
  
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("x")
plt.ylabel(" Integrand")
plt.title("Integrand for various values of s")
  
# Adding legend, which helps us recognize the curve according to it's color
plt.legend()
  
# To load the display window
plt.show()

