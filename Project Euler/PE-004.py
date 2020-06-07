#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Largest palindrome product

Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
max_palindrome=[11,11,121] # just an arbitrary small product palindrome

for i in range(100,999):
    for j in range(i,1000):
        pr=str(i*j)
        # test if it is a palindrome...
        if pr==pr[::-1] : # the [::-1] reverses a string
            if i*j > max_palindrome[2]:
                max_palindrome=[i,j,i*j]

print(max_palindrome)



