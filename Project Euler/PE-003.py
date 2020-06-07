#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Largest prime factor
  
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

"""
The first non-trivial factor will be prime. Let us write a function to 
find that. 
"""

def first_factor(n):
    for i in range(2,1+int(n**(0.5))):
        if n % i == 0: return(i)
    else: return(n)

# now let's write a function that generates a list of prime factors

def prime_factors(n,list_of_factors=[]):
    #print(n,list_of_factors)
    ff = first_factor(n)
    if ff==n: return list_of_factors.append(n)
    else:
        list_of_factors.append(ff)
        prime_factors(n//ff,list_of_factors)
    return(list_of_factors)


print(prime_factors(600851475143,[]))
