"""Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene
que evaluar la cadena y decir cuantas letras mayúsculas tiene."""
# Creamos una variable con el valor que introducimos
print ("Introduce una palabra")
palabra = input()
# Definimos una funcion que mirará todas las letras de la palabra y si no es minuscula sumará 1 al contador
def mayus (palabra):
    contador = 0
    for i in palabra:
        if i !=i.lower():
            contador+=1
    return contador
# Muestra en pantalla el resultado de la funcion
print(mayus(palabra))