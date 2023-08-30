# Ejercicio 7
# Defina la clase EmpleadoPorHora la clase permite almacenar
# el nombre del empleado, el nombre del lugar donde trabaja, el precio
# por hora y la cantidad de horas que trabaja.



class EmpleadoPorHora:
	def __init__(self, nb, tr, precio, ht):
		self.nombre = nb
		self.lugar = tr
		self.pph = precio
		self.cantH = ht

	def getNombre(self):
		return self.nombre

	def getLugar(self):
		return self.lugar

	def getPrecio(self):
		return self.pph

	def getCantH(self):
		return self.cantH

	def setNombre(self, nuevo):
		self.nombre = nuevo

	def setLugar(self, nuevo):
		self.lugar = nuevo

	def setPrecio(self, nuevo):
		self.pph = nuevo

	def setCantH(self, nuevo):
		self.cantH = nuevo

	def dineroTotal(self):
		return (self.pph * self.cantH)