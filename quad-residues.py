#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
We look at quadratic residues
"""

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 47]

# This will be a dictionary with the primes and their quadratic residues:
quad_rezzes = {} 

for p in primes:
    quad_res = [] # will be a list of quad residues for the current prime
    for i in range(p):
        quad_res.append(i**2 % p)
    quad_rezzes.update({p : quad_res})

print(quad_rezzes)

for p in primes:
    print(p,len(set(quad_rezzes[p])))

