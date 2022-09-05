# -*- coding: utf-8 -*-
"""
sum of digits
"""

n = int(input("Digite um número inteiro: "))

sum_of_digits = 0

while n>0:
    sum_of_digits = sum_of_digits + n % 10
    n = n // 10


print(sum_of_digits)