"""
Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga
"""
lista=[]
def larga(x):
    largo = 0
    for i in x:
        len(i)
        if len(i) >= largo:
            largo = len(i)
            palabra = i

    return palabra,largo

print("Introduce la palabra para añadir a la lista")
palabra=input()
while palabra!= "":
    lista.append(palabra)
    print("Introduce otra palabra para añadirlo a la lista")
    palabra= input()

print("La palabra con mayor longitud es ",larga(lista))