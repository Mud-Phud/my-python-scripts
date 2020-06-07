# -*- coding: utf-8 -*-
"""
We write a short code for lexographical ordering
"""
import numpy as np

alpha = np.int16([5,3,3,2])
beta = np.int16([5,3,1,3])

# want to define a function that outputs the first non-zero element
# of an array

def sign_first_nonzero(a):
    for i in range(len(a)):
        if a[i] != 0:
            if a[i] > 0:
                return +1
            else: return -1
    return 0
    
def lex_order(a,b):
    if sign_first_nonzero(a-b) == +1:
        print(str(a) + " > " + str(b))
    if sign_first_nonzero(a-b) == 0:
        print(str(a) + " = " + str(b))
    if sign_first_nonzero(a-b) == -1:
        print(str(a) + " < " + str(b))