######################### ENCARGADO #########################
#Modela a un encargado para el sistema. Un encargado puede crear y eliminar inscripciones
#Ademas puede modificar cualquier dato de una inscripcion excepto su nota

import Inscripcion

class Encargado:
	def __init__(self, nombre, dni):
		self._nombre = nombre
		self._dni = dni

	def getNombre(self):
		return self._nombre

	def getDNI(self):
		return self._dni

	def setNombre(self, nuevoNombre):
		self._nombre = nuevoNombre

	def setDNI(self, nuevoDNI):
		self._dni = nuevoDNI

	def incorporarInscripcion(fecha, alumno, materia, profesor, curso, division, dicInscripciones):
		nuevaInscripcion = Inscripcion(fecha, alumno, materia, profesor, curso, division)
		if(nuevaInscripcion not in dicInscripciones.values()):
			dicInscripciones[fecha + alumno + materia] = nuevaInscripcion
		
	def eliminarInscripcion(inscripcion, dicInscripciones):
		dicInscripciones.pop(inscripcion.getFecha() + \
			inscripcion.getAlumno() + inscripcion.getMateria())
		
	def modificarFecha(inscripcion, nuevaFecha):
		inscripcion.setFecha(nuevaFecha)

	def modificarAlumno(inscripcion, nuevoAlumno):
		inscripcion.setAlumno(nuevoAlumno)

	def modificarMateria(inscripcion, nuevaMateria):
		inscripcion.setMateria(nuevaMateria)

	def modificarProfesor(inscripcion, nuevoProfesor):
		inscripcion.setProfesor(nuevoProfesor)

	def modificarCurso(inscripcion, nuevoCurso):
		inscripcion.setCurso(nuevoCurso)

	def modificarDivision(inscripcion, nuevaDivision):
		inscripcion.setDivision(nuevaDivision)