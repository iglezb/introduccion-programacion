"""
Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
"""
# Creamos una tupla en la que almacenamos unas edades fijas
edades = (46,32,17,9,63,23,20,15,8,10)
# Pedimos al usuario introducir una edad
edad = int(input("Introduce una edad "))
# Definimos una función en la que dirá cuantas personas tienen mas años que el introducido
def mayores(edades):
    contador = 0
    for i in edades:
        if i > edad:
            contador +=1
    return contador
# Muestra en pantalla el resultado llamando a la funcion
print(mayores(edades))