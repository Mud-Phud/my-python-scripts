#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 19:58:33 2020

@author: robert
"""
import numpy as np

y= np.array([3,4,0,0,5,0])
f = lambda x: int(bool(x)) # converts non-zero to 1 and zero to zero. 

y_int = np.array([f(i) for i in y])
#
#print(y_int)