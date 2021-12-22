"""
Definir un histograma procedimiento() que tome una lista de números enteros e
imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir
lo siguiente:
"""
# Definimos una funcion en la que repetirá * por el numero que hay en la lista
def procedimiento(lista):
    for i in lista:
        print("*"*i)
# Definimos las variables de lista en la que añadimos distintos numeros
lista = []
# Se utiliza la funcion int para que lo que introduzcamos no sea una cadena
numero = int(input("Introduce un numero "))
# Se pedirá añadir un numero hasta que introduzcames un 0
while numero != 0:
    # Utilizando .append se añadirán los numeros a la lista
    lista.append(numero)
    numero = int(input("Introduce otro numero o 0 para cancelar"))
# Llamamos a la función utilizando la lista que hemos creado y muestra el resultado
procedimiento(lista)