#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Euclidean algorithm for integers

Created on Sun Jan 10 04:22:45 2021

@author: robert
"""

def EucAlg(a,b):
    print("a,b = ",a,b)
    if a == b:
        return a
    # will make a the smaller number...
    if a>b:
        c = b
        b = a
        a = c
    print(a,b, " b mod a = ", b % a)
    if b % a == 0:
        return a
    else:
        return EucAlg(b % a, a)

