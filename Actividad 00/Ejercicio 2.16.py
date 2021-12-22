"""
Definir una lista con un conjunto de nombres, imprimir la contador de comienzan con la
letra a.
También se puede hacer elegir al usuario la letra a buscar. (Un poco mas emocionante)
"""
# Creamos la lista a la que añadiremos valores
nombres = []
# Creamos un bucle para introducir los nombres para añadir a la lista
for x in range(1,10):
	nombres.append(input("Introduce un nombre : ").lower())
# Solicitamos que letra queremos buscar al principio del nombre
busqueda = input("Introduce la letra que quieres buscar: ").lower()
contador = 0
# Creamos un bucle que mirará cada nombre de la lista y mirará si coincide la primera letra con la introducida y si coincide pasa al siguiente nombre
for nombre in nombres:
	for letra in nombre:
		if letra == busqueda:
			contador = contador + 1
			break
# Muestra en pantalla cuantos nombres hay que empiezan por la letra introducida
print(contador)