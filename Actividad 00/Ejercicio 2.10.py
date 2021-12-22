"""
La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio
2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos
más de 3 números o no sabemos cuántos números son. Escribir una función
max_in_list() que tome una lista de números y devuelva el más grande.
"""
# Creamos la lista en la que añadiremos valores
lista = []
# Definimos una funcion en la que se guardará en la variable valor el numero mayor
def maxlist(x):
    valor = 0
    for i in x:
        if i >= valor:
            valor = i
    return valor
# Añadimos valores a la lista
print("Introduce un numero para añadirlo a la lista ")
seguir = str(input())
numero=int(seguir)
while seguir != "":
    numero = int(seguir)
    lista.append(numero)
    print("Introduce otro numero para añadirlo a la lista")
    seguir = str(input())
# Mostramos en pantalla el resultado con el siguiente mensaje
print ("El valor máximo de la lista es ",maxlist(lista))