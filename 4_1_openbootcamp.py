""" 
Enunciado del ejercicio:
Escribe un programa que pregunte al usuario su edad y
muestre por pantalla si es mayor de edad o no.
"""

print(f"###############################################\n\n\
Ingrese su Edad")

edad = int(input("Edad: "))

if edad > 17:
    print(f"Tienes: {edad} años, Es Mayor de edad")
else:
    print(f"Tienes: {edad} años, Es menor de edad\n")
