######################### PROFESOR #########################
#Modela a un profesor en el sistema. Un profesor puede modificar las notas
#de los alumnos en las inscripciones y ademas puede eliminar las notas
#de una inscripcion. Estas funciones solo sirven si el profesor dicta
#la misma materia que la inscripcion que desee editar

import Inscripcion

class Profesor:
	def __init__(self, nombre, materia, curso, division):
		self._nombre = nombre
		self._materia = materia
		self._curso = curso
		self._division = division

	def getNombre(self):
		return self._nombre

	def getMateria(self):
		return self._materia

	def getCurso(self):
		return self._curso

	def getDivision(self):
		return self._division

	def setNombre(self, nuevoNombre):
		self._nombre = nuevoNombre

	def setMateria(self, nuevaMateria):
		self._materia = nuevaMateria

	def setCurso(self, nuevoCurso):
		self._curso = nuevoCurso

	def setDivision(self, nuevaDivision):
		self._division = nuevaDivision

	def modificarNota(inscripcion, nuevaNota):
		inscripcion.setNota(nuevaNota)

	def eliminarNota(inscripcion):
		inscripcion.setNota(-1)