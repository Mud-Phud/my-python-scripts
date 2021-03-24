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
x, y, z = symbols('x, y, z')


def DivAlg(fs,f,mon_ord):

    
    s = len(fs)
    a = [0]*s
    
    r = 0
    p = f
    
    while p != 0:
        i = 0                # indexing in python begins at 0, not 1
        divisionoccurred = False
        while ( i <= s - 1) and (divisionoccurred == False ):
            if quo(LT(p,x,y,z,order = mon_ord),LT(fs[i],x,y,z,order = mon_ord) ) != 0:
                LT_quot = simplify(LT(p,x,y,z,order = mon_ord) / LT( fs[i],x,y,z,order = mon_ord ))
                a[i] += LT_quot
                p += - expand( LT_quot * fs[i] )
                divisionoccurred = True
            else:
                i += 1
        if divisionoccurred == False:
            r += LT (p,x,y,z,order = mon_ord)
            p += - LT (p,x,y,z,order = mon_ord)
                
    return([a,r])

print(DivAlg([x * y -1, y**2 - 1 ],x**2 * y + x * y**2 + y**2,'lex') ) 
