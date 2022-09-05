# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
primo = True

n = int(input("Digite um número inteiro: "))

fator_poss = 2
while primo == True and fator_poss < n//2  + 1:
    
    if n % fator_poss == 0:
        primo = False
    fator_poss = fator_poss + 1
    
    
if primo:
    print("primo")
else:
    print("não primo")