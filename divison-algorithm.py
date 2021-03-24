#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The division algorithm

Pseudo code...

Input: g, f
Output: q, r
q := 0; r := f
WHILE r = 0 AND LT (g) divides LT (r ) DO
q := q + LT (r )/ LT (g)
r := r − ( LT (r )/ LT (g))g

"""


from sympy import *

x = symbols('x')

f= x**4-5*x**2-2*x+7
g = 3*x**2 + 4*x - 2

q = 0 
r = f
while (r != 0 & degree(g) < degree(r) ):
    q = q + LT (r )/ LT (g)
    r = r - ( LT (r )/ LT (g))*g
    
print(q,r)



