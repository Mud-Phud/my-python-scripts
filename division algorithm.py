#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Division algorithm and Euclidean algorithm in Sympy
The pseudo-code for this...

Input: g, f
Output: q, r
q := 0; r := f
WHILE r != 0 AND LT (g) divides LT (r ) DO:
    q := q + LT (r )/ LT (g)
    r := r − ( LT (r )/ LT (g))g
"""

from sympy import *

x = symbols('x')

f=x**4-x**3-4*x**2-5*x-3
g=x**2+3*x-5

q = 0
r = f

while (r != 0) & (degree(g) <= degree(r)):
    q = q + LT(r)/LT(g) 
    r = r - expand(( LT(r)/LT(g)) * g)
    

print("quotient = ",q,", remainder = ",r)

def DivAlg(f,g):
    q = 0
    r = f

    while (r != 0) & (degree(g) <= degree(r)):
        q = q + LT(r)/LT(g) 
        r = r - expand(( LT(r)/LT(g)) * g)
        
    return [q,r]