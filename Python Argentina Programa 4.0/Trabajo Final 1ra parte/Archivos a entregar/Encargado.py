######################### ENCARGADO #########################
#Modela a un encargado para el sistema. Un encargado puede crear y eliminar inscripciones
#Ademas puede modificar cualquier dato de una inscripcion excepto su nota

import Inscripcion

def crearEncargado(nombre, dni):
	return {"nombre": nombre, "dni": dni}

def getNombre(encargado):
	return encargado["nombre"]

def getDNI(encargado):
	return encarado["dni"]

def setNombre(encargado, nuevoNombre):
	encargado["nombre"] = nuevoNombre

def setDNI(encargado, nuevoDNI):
	encargado["dni"] = nuevoDNI

def incorporarInscripcion(fecha, alumno, materia, profesor, curso, division, dicInscripciones):
	nuevaInscripcion = Inscripcion.crearInscripcion(fecha, alumno, materia, profesor, curso, division)
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