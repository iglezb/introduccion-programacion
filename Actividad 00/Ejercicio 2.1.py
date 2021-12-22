"""
Definir una función max() que tome como argumento dos números y devuelva el mayor
de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla
nosotros mismos es un muy buen ejercicio.
"""
#Introducimos los valores en variables
valor1 = int(input("Introduce el primer valor "))
valor2 = int(input("Introduce el segundo valor "))
# Definimos una función que compara los valores y muestra el resultado. #
def maxi(valor1,valor2):
   if valor1 > valor2:
       print("El mayor valor es ",valor1)
   else:
        print("El mayor valor es ",valor2)
# Llamamos a la función que hemos definido para que se realice dicha funcion #
maxi(valor1,valor2)