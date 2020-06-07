#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sum square difference

Problem 6
The sum of the squares of the first ten natural numbers is,

1**2+2**2+...+10**2=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)**2=552=3025
Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
"""


# There is a formula for the sum of squares:

print("n","Sum i**2","(2*n+1)*(n+1)*n/6")
for n in range(1,10):
    sum=0
    for i in range(n+1):
        sum = sum + i*i
    print(n,sum,(2*n+1)*(n+1)*n//6)
    
# The sum of the first n intergers is just n*(n+1)/2. Thus, the answer
# is ( n*(n+1)/2 )**2 - (2*n+1)*(n+1)*n//6

n = 100
print( ( n*(n+1)//2 )**2 - (2*n+1)*(n+1)*n//6 )

# let's do this the naive way. To make it slightly faster, we
# vectorize it ...

import numpy as np
a = np.arange(101)

print(np.sum(a)**2-np.sum(a*a))
