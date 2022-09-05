# -*- coding: utf-8 -*-
"""
factorial
"""

n = int(input("Digite o valor de n: "))

if n == 0 or n == 1: print(1)
else:
    factorial = 1
    i = 1
    while i <= n:
        factorial = factorial * i
        i = i + 1
    print(factorial)