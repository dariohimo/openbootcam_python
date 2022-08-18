""" 
Escribe un programa capaz de mostrar todos los
 números impares desde un número de inicio y otro final.

Por ejemplo: teniendo numero_inicial = 2
y numero_final = 8,  el programa debe imprimir
 por consola: [3, 5, 7]
"""

print(f"###############################################\n\n\
Ingrese número inicial y final")

inicio = int(input("Número Inicial: "))

final = int(input("Número Final: "))

numeros = []

for x in range( inicio, final):
   if x % 2 != 0:
      numeros.append(x)
   
print(f"{numeros}")
