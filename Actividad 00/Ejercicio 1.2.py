"""
Solicitar al usuario dos valores:
● numero1 (int)
● numero2 (int)
Se debe imprimir el mayor de los dos números (la salida debe ser idéntica a la que
sigue):
Proporciona el numero1:
Proporciona el numero2:
El numero mayor es:<numeroMayor>
¿Cuál es el código del requerimiento solicitado? """
# Se solicita al usuario que introduzca los valores que queremos comparar
numero1 = int(input('Introduce el primer valor '))
numero2 = int(input('Introduce el segundo valor '))
# Utilizando un condicional y una operación logica comparamos que valor es mayor de los dados por el usuario
if numero1 > numero2:
    print('El numero mayor es ',numero1)
else:
    print('El numero mayor es ', numero2)