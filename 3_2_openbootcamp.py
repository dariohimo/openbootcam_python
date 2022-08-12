""" 
Escribe un programa en la consola de python que pida al usuario su peso (en kg) 
y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable,
e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa
 corporal calculado redondeado con dos decimales. 

 índice de masa corporal (IMC), 
 que se calcula dividiendo los kilogramos de peso 
 por el cuadrado de la estatura en metros (IMC = peso [kg]/ estatura [m2]).
"""
from tokenize import Double


print(f"###############################################\n\
Ingrese su peso en Kilogramos para saber su IMC")

peso = int(input("Su peso: "))
estatura = float(input("Su peso: "))

IMC = peso / estatura **2


print(f"\nTu índice de masa corporal es: {IMC:.2f}\n ")