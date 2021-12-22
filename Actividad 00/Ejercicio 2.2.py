"""
Definir una función max_de_tres(), que tome tres números como argumentos y
devuelva el mayor de ellos.
"""
# Introducimos los valores en variables distintas #
valor1 = int(input("Introduce el primer valor "))
valor2 = int(input("Introduce el segundo valor "))
valor3 = int(input("Introduce el tercer valor "))
#Definimos la función que compara el primer valor con los otros y si este no es mayor comparará el siguiente con los otros valores #
def maxi(valor1,valor2,valor3):
    if valor1 >= valor2 and valor1 >= valor3:
     print("El mayor valor es ",valor1)
    elif valor2 >= valor1 and valor2 >= valor3:
       print("El mayor valor es ",valor2)
    elif valor3 >= valor1 and valor3 >= valor2:
       print("El mayor valor es ", valor3)
#Llamamos a la función para mostrar el resultado en pantalla #
maxi(valor1,valor2,valor3)