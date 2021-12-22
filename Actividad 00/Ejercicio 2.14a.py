"""
Construir un pequeño programa que convierta números binarios en enteros.
"""
# Introducimos un numero binario que almacenaremos en una variable
print("Introduce un número binario")
binario = input()
# Definimos la funcion que calculará el resultado utilizando una operacion con base 2
def calculo (binario):
    decimal = 0
    for i in binario:
        decimal = decimal*2 + int(i)
    return decimal
# Mostramos en pantalla el resultado
print(calculo(binario))
