"""
Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400
"""
# Definimos la funcion que dividirá el año introducido entre 4 y que no ea entre 100 y el resultado significara que es un año bisiesto
def bisiesto(año):
    if año%4 == 0 and año%100 != 0:
      print("El",año,"es bisiesto")
    else:
        print("El año",año,"NO es bisiesto")
# Solicitamos al usuario el año
año= int(input("Introduce un año: "))
# Llamamos a la funcion
bisiesto(año)