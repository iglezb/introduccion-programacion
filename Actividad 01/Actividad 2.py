'''
Crearemos un programa el cual tratará de adivinar el número aleatorio que
generaremos entre 1 y 10. Nuestro objetivo es adivinar el número. Si fallamos nos dirán si
es mayor o menor que el número buscado. También el programa nos deberá de indicar
el número de intentos requeridos.
'''
# Importamos la libreria random de python #
import random
# Definimos las variables de intentos y el número que se generará de forma aleatoria
aleatorio = random.randint(1,10)
intentos = 0
# Creamos un bucle que vaya sumando los intentos hasta llegar a 5 y si adivina el numero acabar.
while intentos < 5:
    numero = int(input("Introduce un numerito "))
    intentos += 1
    if numero == aleatorio:
        print("¡Has adivinado el numerito!")
        break
    if numero > aleatorio:
        print("El número que has introducido es mayor")
    if numero < aleatorio:
        print("El número que has introdicdo es menor")
