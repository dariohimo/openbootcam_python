#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Escribe una función que pueda decirte si un número
(número entero) es primo o no.
"""
print(f"   ############################################### \n")

def numero_primo(num):
    if num < 2:
        return False           
    for i in range(2, num):
        if num % i == 0:
           return False          
    return True                   


num = int(input("ingresa un número: "))

if numero_primo(num):
    print(f"El número entero {num}, Es primo.\n")
else:
    print(f"El número entero: {num}, No es primo.\n")

    






