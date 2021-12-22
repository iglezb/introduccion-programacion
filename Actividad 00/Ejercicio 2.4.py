"""
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
contrario devuelve False.
"""
# Definimos una función en la que compara la letra introducida con todas las vocales
def vocal(x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True #Si la letra introducida es vocal devolverá True
    elif x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return True
# Crearemos una variable con la letra que introducimos
letra = input("Introdue una letra ")
# Llamamos a la funcion y lo mostramos por pantalla
print(vocal(letra))