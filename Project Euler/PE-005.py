#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Smallest multiple

Problem 5
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?

Note that one can solve this by factoring the numbers from 2 to 20 and 
taking the 

2,3,2**2,5,2*3,7,2**3,3**2,2*5,11,2**2*3,13,2*7,3*5,2**4,17,2*3**2,19,2**2*5

to obtain the LCM:
"""
print(2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19)


# but let us do it using a naive search. We need a function that determines
#  if a number is divisible by 2 through 20. 

def is_div_20(n):
    for i in range(2,21):
        if n % i != 0: return False
    return True

# now we know that the product of 1 through 20 is divisible by 1 through 20.
# this is just 20! We can use this as an upper bound. 

import math
max_upper_bound = math.factorial(20)
    
for i in range(2,max_upper_bound+1):
    if is_div_20(i):
        print(i)
        break

# it takes a while! We can time the process using the following:
        
import timeit
code_to_test = """
import math
max_upper_bound = math.factorial(20)
    
for i in range(2,max_upper_bound+1):
    if is_div_20(i):
        print(i)
        break
"""
elapsed_time = timeit.timeit(code_to_test)
print(elapsed_time)