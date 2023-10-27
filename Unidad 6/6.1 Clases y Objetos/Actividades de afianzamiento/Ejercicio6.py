# Ejercicio 6
# Defina la clase Persona. La clase permite registrar el nombre
# y la edad de una persona. Luego escriba un programa principal que
# permita que el usuario ingrese n personas a una lista. Finalmente, el
# programa debe imprimir la lista por pantalla.


class Persona:
	def __init__(self, nb, ed):
		self.nombre = nb
		self.edad = ed

	def getNombre(self):
		return self.nombre

	def getEdad(self):
		return self.edad

	def setNombre(self, nuevo):
		self.nombre = nuevo

	def setEdad(self, nuevo):
		self.nombre = nuevo

	def imprimir(self):
		print("Nombre:", self.nombre, "- Edad:", self.edad)

def ingresarPersonas(cantidad):
	lista = []
	for i in range(cantidad):
		try:
			print("Ingrese el nombre de una nueva persona a agregar:")
			nombre = input()
			print("Ingrese la edad de esa persona:")
			edad = int(input())
			nuevaPersona = Persona(nombre, edad)
			lista.append(nuevaPersona)
		except ValueError:
			print("Se ingreso una edad no valida, no se pudo agregar a esa persona!")
	return lista

loop = True
while(loop):
	try:
		print("Ingrese la cantidad de personas que desee ingresar:")
		cant = int(input())
		lista = ingresarPersonas(cant)
		for persona in lista:
			persona.imprimir()
		loop = False
	except ValueError:
		print("La cantidad ingresada no es un numero, intente de nuevo")