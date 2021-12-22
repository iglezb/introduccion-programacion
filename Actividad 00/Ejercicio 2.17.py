"""
Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a"
tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.
"""
# Definimos la función que va a mirar si la letra es vocal
def vocales(palabra):
    contadora = 0
    contadore = 0
    contadori = 0
    contadoro = 0
    contadoru = 0
    # Utilizamos un bucle para que mire cada letra de la palabra y comprobará si es igual a una vocal y sumará el contador de esa vocal
    for i in palabra:
        if i == "a":
            contadora +=1
        elif i == "e":
            contadore += 1
        elif i == "i":
            contadori += 1
        elif i == "o":
            contadoro += 1
        elif i == "u":
            contadoru += 1
    print("Tiene", contadora, "a")
    print("Tiene", contadore, "e")
    print("Tiene", contadori, "i")
    print("Tiene", contadoro, "o")
    print("Tiene", contadoru, "u")
# Introducimos la palabra y la transformaremos a minuscula para la comparacion
palabra= input("Introduce una palabra: ").lower()
# Muestra el resultado utilizando el siguiente formato
vocales(palabra)