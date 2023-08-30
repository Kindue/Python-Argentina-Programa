# Ejercicio 3
# Escriba un programa principal que:
# 1. Inserte en una lista n personas.
# 2. Almacene en una lista la/s persona/s de mayor edad.
# 3. Imprima la lista.
# Nota: Luego de haber resuelto este ejercicio reflexione respecto de
# las ventajas de haberlo realizado usando el concepto de Tipo de Dato
# Abstracto

import Ejercicio2

def ingresarPersonas(cantidad):
	lista = []
	for i in range(cantidad):
		try:
			print("Ingrese el nombre de una nueva persona a agregar:")
			nombre = input()
			print("Ingrese la edad de esa persona:")
			edad = int(input())
			nuevaPersona = Ejercicio2.crearPersona(nombre, edad)
			lista.append(nuevaPersona)
		except ValueError:
			print("Se ingreso una edad no valida, no se pudo agregar a esa persona!")
	return lista

def contarMayor(l):
	lista = []
	mayor = 0
	for persona in l:
		if(Ejercicio2.getEdad(persona) >= mayor):
			mayor = Ejercicio2.getEdad(persona)
	for persona in l:
		if(Ejercicio2.getEdad(persona) == mayor):
			lista.append(persona)
	return lista

loop = True
while(loop):
	try:
		print("Ingrese la cantidad de personas que desee ingresar a una lista:")
		cant = int(input())
		listaPersonas = ingresarPersonas(cant)
		listaMayores = contarMayor(listaPersonas)
		for persona in listaMayores:
			Ejercicio2.imprimir(persona)
		loop = False
	except ValueError:
		print("La cantidad ingresada no es un numero, por favor intentelo de nuevo")