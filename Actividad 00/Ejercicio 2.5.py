"""
Escribir una función sum() y una función multip() que sumen y multipliquen
respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería
devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""
total=0
multiplo = 1
lista = []
# Definimos la función de suma donde se sumará todos los valores que se vayan introduciendo
def sumita (x):
    for i in lista:
        global total
        total += i
    return total
# Definimos la función de multiplicacion que multiplicará los valores que se van introduciendo
def multip (x):
    for i in lista:
        global multiplo
        multiplo = multiplo * i
    return multiplo
# Se muestra un menu en el que segun la opción realizará dicha función
print("""
Introduce el número de la funcion
1. Sumar    2. Multiplicar  3. Cerrar
""")
opcion = input()
# Si se introduce la opcion de suma iniciará la funcion
if opcion == "1":
    print("Introduce número para añadir a la suma")
    numero = int(input())
# Seguirá solicitando numeros que añadir hasta que dejemos el campo en blanco y mostrará el resultado total
    while numero != "":
        lista.append(numero)
        print("Introduce otro numero para añadir a la suma")
        numero = input()
    lista = [int(i) for i in lista]
    print("El total de la suma es ",sumita(lista))
# Introduciendo la opcion de multiplicar solicitará los numeros que queremos multiplicar hasta que dejemos el espacio en blanco
elif opcion == "2":
    print("Introduce número para añadir a la multiplicacion")
    numero = int(input())
    while numero != "":
        lista.append(numero)
        print("Introduce otro numero para añadir a la suma")
        numero = input()
# Modificamos la lista para que sean interger o numeros y no cadenas o string
    lista = [int(i) for i in lista]
    print("El total de la multiplicacion es ", multip(lista))