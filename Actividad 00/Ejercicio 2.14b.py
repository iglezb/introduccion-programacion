"""
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
"""
# Creamos un diccionario en la que iremos almacenando una clave:valor
persona = {}
# Solicitamos introducir el año en curso y lo almacenamos en una variable
print("Ingresa el año en curso")
añocurso=int(input())
# Hacemos un bucle para que solicite los nombres y año de nacimiento 3 veces.
for i in range(0,3):
    # Introducimos los valores de la persona
    nombre= input("Introduce un nombre: ")
    año = int(input("Introduce año de nacimiento: "))
    # Se almacena una pareja de clave:valor
    persona[nombre] = año
    resultado = añocurso - año
    # Muestra el resultado en pantalla
    print(nombre,"cumplirá ",resultado,"años")