#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
We define the function that uses the division algorithm then
the function that finds the Greatest Common Divisor

We use the pseudocode 

Input: f, g
Output: h
h := f
s := g
WHILE s != 0 DO
    rem := remainder(h, s)
    h := s
    s := rem
"""

from sympy import *

x = symbols('x')

f=x**4-x**3-4*x**2-5*x-3
g=x**2+3*x-5


# the division algorithm, returns the quotient and remainder

def DivAlg(f,g):   
    q = 0   # quotient
    r = f   # remainder

    while (r != 0) & (degree(g) <= degree(r)):
        q = q + LT(r)/LT(g) 
        r = r - expand(( LT(r)/LT(g)) * g)
        
    return [q,r]

def GCDalg(f,g):
    h = f
    s = g
    while (s!= 0):
        r = DivAlg(h,s)[1]
        h = s
        s = r
    return h/LC(h)

print(GCDalg(x**3-x**2-x-2,x**4-x**3-4*x**2-5*x-3))

    
