"""
Iterar un rango de 0 a 10 e imprimir sólo los números divisibles entre 3
"""
# Se crea un bucle que va desde el 0 hasta el 10.
for i in range(0,10):
    if i == 0:
        continue
# Comprueba que el numero es divisible entre 3 dando un resto 0 y muestra que dicho numero es divisible
    if i%3 == 0:
        print(i,' es divisible entre 3')