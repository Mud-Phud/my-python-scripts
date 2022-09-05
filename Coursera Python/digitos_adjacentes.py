# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
diferente = True

n = int(input("Digite um número inteiro: "))

while n != 0 and diferente == True:
    i1 = n % 10
    n = n // 10
    i2 = n % 10
    if i1 == i2:
        diferente = False
    
if diferente:
    print("não")
else:
    print("sim")