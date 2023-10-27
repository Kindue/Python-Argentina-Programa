# Ejercicio 2
# Implemente el tipo de dato abstracto Persona. Los datos que
# se desean registrar de una persona son: el nombre y la edad.


def crearPersona(nombre, edad):
	return [nombre, edad]

def getNombre(persona):
	return persona[0]

def getEdad(persona):
	return persona[1]

def setNombre(persona):
	persona[2]

def setEdad(persona):
	persona[1]

def imprimir(persona):
	print("Nombre:", persona[0], "Edad:", persona[1])