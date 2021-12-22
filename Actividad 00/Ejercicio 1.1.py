"""
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionará un valor entre 0 y 10.
Si está entre 9 y 10: imprimir una A
Si está entre 8 y menor a 9: imprimir una B
Si está entre 7 y menor a 8: imprimir una C
Si está entre 6 y menor a 7: imprimir una D
Si está entre 0 y menor a 6: imprimir una F
cualquier otro valor debe imprimir: Valor desconocido
Por ejemplo:
Proporciona un valor entre 0 y 10:
"""
# Se creará una variable con la nota que introduciremos
nota = float(input('Introduce una nota '))
# Se creará una condicional y dependiendo del valor mostrará un resultado u otro  y lo muestra por pantalla
# Si la nota introducida está entre un rango mostrará dicho resultado
if nota >=9 and nota <=10:
    print('La nota es A')
if nota >=8 and nota <9:
    print('La nota es B')
if nota >=7 and nota <8:
    print('La nota es C')
if nota >=6 and nota <7:
    print('La nota es D')
if nota >=0 and nota <6:
    print('La nota es F')