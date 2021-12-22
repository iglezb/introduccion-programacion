"""
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y
devuelva las palabras que tengan más de n caracteres.
"""
# Creamos la lista en la que le añadiremos valores
lista=[]
# Creamos una funcion en la que medirá la longitud de la palabra y comprobará si la longitud es mayor o igual al numero introducido
# Si la palabra es mayor se almacenará en la variable
def larga(x):
    palabra=""
    for i in x:
        len(i)
        if len(i) >= numero:
            palabra = palabra + "|" + i
    return palabra
# Pedimos al usuario introducir palabras para añadir a la lista
print("Introduce la palabra para añadir a la lista")
palabra=input()
while palabra!= "":
    lista.append(palabra)
    print("Introduce otra palabra para añadirlo a la lista")
    palabra= input()
# Pedimos al usuario el numero para mostrar las palabras con una longitud mayor a esta
print("Introduce el valor para mostrar la palabra con una longitud mayor")
numero = int(input())
# Mostramos el resultado en pantalla
print("La palabra o las palabras con mayor longitud son ",larga(lista))