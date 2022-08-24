""" 
Escribe una función que pueda decirte si un año 
(número entero) es bisiesto o no.
Un año es bisiesto si es:

Divisible entre 4.
No divisible entre 100.
Divisible entre 400.
(2000 y 2400 son bisiestos pues aún siendo divisibles entre 100
lo son también entre 400.
Pero los años 1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600
no lo son porque sólo son divisibles entre 100).
"""
print(f"   ############################################### \n")
import calendar
def esBisiesto(num):
    return calendar.isleap(num)

def bisiesto(num):
    return num % 4 == 0 and num % 100 != 0 or num % 400 == 0


num = int(input("Si es o No bisiesto un Año: "))
 
if bisiesto(num):
    print(f"año bisiesto: {num}")
else:
    print(f"No es bisiesto: {num}")

print(f"Año, {esBisiesto(num)} {num}")








