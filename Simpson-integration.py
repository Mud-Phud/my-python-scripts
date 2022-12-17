#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 05:26:10 2022

Simpson's method for approximation of integrals

"""
import numpy as np

def my_sin(x):
    return np.sin(x)

def ident(x):
    return x

def squared(x):
    return x**2



def Simp(f,a,b,n):
    if n % 2 == 0: n += 1  # n needs to be odd.
    h = (b-a)/(n-1)

    x = np.linspace(a,b,n) 
    y = f(x)
    return (h/3)*(2*sum(y[::2])-y[0]-y[-1] + 4*sum(y[1::2]))

print(Simp(ident,0,1.0,7))

print(Simp(squared,0,1,6))

print(Simp(my_sin,0,3.14159,6))

# Let's use Simpson to caculate the gamma fnciton

def integrand(t,z):
    return t**(z-1)*np.exp(-t)

print(integrand(3,1.5))


def Gamma(z):
    if z.real > 2: 
        return (z-1)*Gamma(z-1)
    elif z.real < 1:
        return Gamma(z+1)/z
    else:
        a=0;b=15;n=101
        h = (b-a)/(n-1)
        t = np.linspace(a,b,n) 
        y = integrand(t,z)
        return (h/3)*(2*sum(y[::2])-y[0]-y[-1] + 4*sum(y[1::2]))

z = np.linspace(.1,5,100)
y = []
for x in z:
    y.append(Gamma(x))

    

import matplotlib.pyplot as plt
plt.plot(z,y)
plt.ylabel('Gamma function')
plt.show()

