#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Summation of primes
  
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

We do this by making a "sieve or Erasthones"
"""
import numpy as np

N=2000000
primes_list = np.arange(N+1) # a list with the i-th entry equal to i.

primes_list[1]=0

# to test if a number is prime, you only need to test for divisors up to 
# the square root...
max_test = int(N**(0.5))  

for i in range(2,max_test):
    #print(i,primes_list)
    if primes_list[i] != 0:  # then i is prime. Need to eliminate multiples...
        for j in range(2,N//i+1):
            primes_list[j*i]=0 

print(np.sum(primes_list))

