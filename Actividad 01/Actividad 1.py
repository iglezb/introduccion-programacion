"""
Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que
tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría
que devolver True
"""
# Creamos una funcion que invierte la palabra
def inverso (x):
    inversion =""
    for i in x:
        inversion = i + inversion
    return inversion
# Introducimos la palabra y la almacenamos en una variable
print ("Introduce una frase")
frase=input()
# Comparamos si la palabra introducida es igual a la palabra invertida y mostramos el resultado
if inverso(frase) == frase:
   print("La palabra ",frase,"es igual que invertida",inverso(frase))
else:
    print("La palabra ",frase," no se lee igual en inverso",inverso(frase))