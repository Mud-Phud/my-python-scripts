#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:42:12 2020

@author: robert
"""

from itertools import product

def epsilon(indexes):
    indexes = list(indexes)
    if len(indexes) != len(set(indexes)):
        return 0
    elif indexes == sorted(indexes):
        return 1
    else:
        for i in range(len(indexes)):
            for j in range(len(indexes) - 1):
                if indexes[i] > indexes[j + 1]:
                    indexes[j], indexes[j + 1] = indexes[j + 1], indexes[j]
                    return -1 * epsilon(indexes)

def draw_table(all_cases):
    epsilonValues = []
    for case in all_cases:
        epsilonValues.append(epsilon(case))
    print('| i | j | k ||| L-C')
    print('|===========|||======')
    k = '|___|___|___|||___'
    print(k)
    i = 0
    for case in all_cases:
        a, b, c = str(case[0]), str(case[1]), str(case[2])
        print('| ' + a + ' | ' + b + ' | ' + c + ' ||| '+ str(epsilonValues[i]))
        i += 1
        print(k)

draw_table(list(product([0, 1, 2], repeat=3)))
