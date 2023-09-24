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
		dicInscripciones.pop(Inscripcion.getFecha(inscripcion) + \
			Inscripcion.getAlumno(inscripcion) + Inscripcion.getMateria(inscripcion))
		
	def modificarFecha(inscripcion, nuevaFecha):
		Inscripcion.setFecha(inscripcion, nuevaFecha)

	def modificarAlumno(inscripcion, nuevoAlumno):
		Inscripcion.setAlumno(inscripcion, nuevoAlumno)

	def modificarMateria(inscripcion, nuevaMateria):
		Inscripcion.setMateria(inscripcion, nuevaMateria)

	def modificarProfesor(inscripcion, nuevoProfesor):
		Inscripcion.setProfesor(inscripcion, nuevoProfesor)

	def modificarCurso(inscripcion, nuevoCurso):
		Inscripcion.setCurso(inscripcion, nuevoCurso)

	def modificarDivision(inscripcion, nuevaDivision):
		Inscripcion.setDivision(inscripcion, nuevaDivision)