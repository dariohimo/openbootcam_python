""" 
Escribe una función que calcule el área de un triángulo, 
recibiendo la altura y la base como parámetros 
A = b . h / 2
y otra 
función que calcule el área de un círculo recibiendo el radio del mismo.
A = pi * (r ** 2)
"""
print(f"         ############################################### \n")

b = int(input("ingresa la base del triangulo: \n"))
h = int(input("ingresa la altura del triangulo: \n"))
r = int(input("ingresa el radio del circulo: \n"))
 
def area_triangulo(b, h):
    A = b * h / 2
    return int(A)

def area_circulo(r):
    A = (3.14) * (r**2)
    return (A) 

print(f"Area de un Triangulo es: {area_triangulo(b, h)} ")
print(f"Area de un Circulo es: {area_circulo(r):,.2f} cm\u00b2 \n")