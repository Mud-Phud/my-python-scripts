#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
10001st prime
 
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

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

# this gets rid of the zero elements...
primes_list = primes_list[primes_list != 0] 

print(primes_list[10000])

