"""
Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto
que python tiene la función len() incorporada, pero escribirla por nosotros mismos
resulta un muy buen ejercicio.
"""
# Creamos una lista en la que le introduciremos valores posteriormente
lista = []
# Definimos una funcion en la que si es una palabra contará cuantas letras y si es una lista contará cuantos elementos hay en la lista
def longitud(x):
    contador = 0
    for i in palabra or lista:
        contador += 1
    return contador
# Introducimos una palabra y la almacenamos en dos variables
print("Introduce la palabra para conocer su longitud")
palabra=input()
listado=palabra
# Muestra la longitud de la palabra intruducida utilizando la función que hemos definido anteriormente
print("La longitud de la palabra escrita es ",longitud(palabra))
# Creamos un bucle en la que seguirá pidiendo palabras para añadir a la lista hasta dejar el espacio en blanco
while palabra!= "":
    lista.append(palabra)
    print("Introduce otra palabra para añadirlo a la lista")
    palabra= input()
# Si la lista tiene más de 1 elemento mostrará cuantos elementos hay en la lista y si no muestra la longitud del primer y unico elemento
if longitud(lista) >= 2:
    print("La longitud de la lista es", longitud(lista))
else:
    print("La longitud de la palabra  es ", longitud(palabra))


"""if acceso >= 2:
    print("La longitud de la lista es",longitud(lista))
else:
   print("La longitud de la palabra  es ",longitud(palabra))"""