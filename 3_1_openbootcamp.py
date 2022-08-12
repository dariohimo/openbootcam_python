"""   openbootcam 
 Para este ejercicio tenéis que crear en la consola de python variables 
 que representen los siguientes datos de un contacto:
Nombre
Apellidos
Edad
Email
Teléfono
Casado (verdadero o falso)
Con Hijos (verdadero o falso)
Lista de amigos
Películas vistas (diccionario con clave y valor. El valor será el título de la película)
Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print().
"""


Nombre = "Pedro"
Apellidos = "Gonzalez"
Edad = 43
email = "pedro@gmail.com"
Casado =  True or False
Hijos =   True or False
Amigos = ['Antonio', 'Pedro', 'Carlos']
Peliculas = {
    'Marvel' : 'Love and Thunder',
     'Disney+': 'Yo soy Groot'
}


print(f"\nNombre: {Nombre}\nApellido: {Apellidos}\nEdad: {Edad}\nEmail: {email}\n\
Casado: {Casado}\nHijos: {Hijos}\nAmigos: {Amigos}\nPeliculas: {Peliculas}\n ")
