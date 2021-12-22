"""
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad, DNI,
teléfono y email. Construye los siguientes métodos para la clase:
● Un constructor, donde los datos pueden estar vacíos.
● Los setters y getters para cada uno de los atributos. Importante: hay que validar
las entradas de datos a través de sus correspondientes funciones.
● Método mostrar(): Muestra los datos de la persona.
● Método esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de
edad
"""

# Creamos una clase en la que estará compuesta por los siguientes atributos
class Persona:
    def __init__(self, nombre, edad, dni, telefono, email):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.telefono = telefono
        self.email = email
# Creamos una función para mostrar los atributos de la persona que deseamos con el siguiente formato
    def mostrar(self):
        mostrado = ("nombre: {}, edad: {}, dni: {}, telefono: {}, email: {}")

        print(mostrado.format(self.nombre, self.edad, self.dni, self.telefono, self.email))

persona1 = Persona("Ismael",15,"8678994H","897854323","hola@gmail.com")
# Creamos los getters de cada atributo para que nos muestres el atributo
def nombre(self):
    return self.nombre

def edad(self):
    return self.edad

def dni(self):
    return self.dni

def telefono(self):
    return self.telefono

def email(self):
    return self.email
# Creamos los setters para modificar el atributo
def setnombre(self,x):
    self.nombre = x

def setedad(self,x):
    self.edad = x

def setdni(self,x):
    self.dni = x

def settelefono(self,x):
    self.telefono = x

def setemail(self,x):
    self.email = x
# Definimos una funcion para saber si la persona es mayor de edad utilizando el atributo edad
def mayordeedad(a):
    if a.edad >= 18:
        print(a.nombre,"es mayor de edad porque tiene",a.edad)
    else:
        print(a.nombre, "no es mayor de edad porque tiene", a.edad)
# Llamamos a la función para conocer si es mayor de edad
mayordeedad(persona1)
