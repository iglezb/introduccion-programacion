"""
Definir una función superposicion() que tome dos listas y devuelva True si tienen al
menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando
el bucle for anidado.
"""
# Creamos las variables listas para introducir datos en ellas posteriormente
lista=[]
lista2=[]
# Definimos una función en la recorrerá cada lista revisando si tienen un mismo elemento ambas listas
def superpos(a,b):
    for i in a:
        for j in b:
            if j == i:
                return True
    return False
# Solicitamos al usuario que introduzca los numeros que queremos añadir a la lista
print("Introduce un numero para añadirlo a la lista 1")
numero=input()
# Introducimos numeros en la lista hasta dejar el espacio en blanco
while numero!= "":
    lista.append(numero)
    print("Introduce otro numero para añadirlo a la lista")
    numero= input()
# Introducimos numeros para añadir en la segunda lista
print("Introduce un numero para añadirlo a la lista 2")
numero2=input()
while numero2!= "":
    lista2.append(numero2)
    print("Introduce otro numero para añadirlo a la lista 2")
    numero2= input()

# Llamamos a la función que compara las dos listas y muestra el resultado
print(superpos(lista,lista2))