"""
Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la
cadena "estoy probando" debería devolver la cadena "odnaborp yotse
"""
# Creamos la función que invertirá la palabra introducida
def inverso (x):
    inversion =""
# Utilizando un bucle for introduciremos cada letra en la variable
    for i in x:
        inversion = i + inversion
    return inversion
# Solicitamos al usuario que introduzca el texto que deseamos invertir
print ("Introduce una frase")
frase=input()
# Llamamos a la función de inversión para mostrar el resultado en pantalla
print(inverso(frase))