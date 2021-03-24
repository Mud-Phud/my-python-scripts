#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 04:58:37 2021

@author: robert
"""

# we will use the seive of erasthones algorithm

import numpy as np

N = 1000000

primes = np.arange(start=2, stop=N+1, step=1)
for i in range(0,N-2):
  if primes[i] > N**0.5:
    break
  if primes[i] != 0:
    for j in range(1,N//primes[i]):
      primes[i+j*primes[i]]=0

# print(primes)

non_zero_filter = np.vectorize(bool)(primes)
primes = primes[non_zero_filter]

