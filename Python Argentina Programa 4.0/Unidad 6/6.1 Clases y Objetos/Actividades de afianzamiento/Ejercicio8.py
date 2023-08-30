# Ejercicio 8
# Defina la clase EmpleadoExclusivo. La clase permite registrar
# el nombre del empleado, el lugar donde trabaja y el sueldo que cobra
# por mes.



class EmpleadoExclusivo:
	def __init__(self, nb, tr, sueldo):
		self.nombre = nb
		self.lugar = tr
		self.sueldo = sueldo

	def getNombre(self):
		return self.nombre

	def getLugar(self):
		return self.lugar
	
	def getSueldo(self):
		return self.sueldo
	
	def setNombre(self, nuevo):
		self.nombre = nuevo

	def setLugar(self, nuevo):
		self.lugar
		
	def setSueldo(self, nuevo):
		self.sueldo = nuevo