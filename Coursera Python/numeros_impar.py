# -*- coding: utf-8 -*-
"""
numeros impar
"""

n = int(input("Digite um número inteiro: "))

sum_of_digits = 0

while n>0:
    sum_of_digits = n % 10
    n = n // 10