#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 19:50:22 2018

@author: robert
"""
import numpy as np

tie = np.array([[2,1, 2], [1, 2, 1], [1, 2, 1]], dtype= int)
one_wins = np.array([[2,1, 1], [1, 2, 1], [1, 2, 1]], dtype= int)
two_wins = np.array([[2,1, 2], [1, 2, 1], [1, 2, 2]], dtype= int)

diag1_wins =  np.array([[1,0, 2], [1, 1, 0], [0, 2, 1]], dtype= int)
diag2_wins =  np.array([[1,0, 2], [1, 2, 0], [2, 0, 1]], dtype= int)
