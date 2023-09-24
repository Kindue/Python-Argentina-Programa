######################### PROFESOR #########################
#Modela a un profesor en el sistema. Un profesor puede modificar las notas
#de los alumnos en las inscripciones y ademas puede eliminar las notas
#de una inscripcion. Estas funciones solo sirven si el profesor dicta
#la misma materia que la inscripcion que desee editar

import Inscripcion

def crearProfesor(nombre, materia, curso, division):
	return {"nombre": nombre, "materia": materia, "curso": curso, "division": division}

def getNombre(profesor):
	return profesor["nombre"]

def getMateria(profesor):
	return profesor["materia"]

def getCurso(profesor):
	return profesor["curso"]

def getDivision(profesor):
	return profesor["division"]

def setNombre(profesor, nuevoNombre):
	profesor["nombre"] = nuevoNombre

def setMateria(profesor, nuevaMateria):
	profesor["materia"] = nuevaMateria

def setCurso(profesor, nuevoCurso):
	profesor["curso"] = nuevoCurso

def setDivision(profesor, nuevaDivision):
	profesor["division"] = nuevaDivision

def modificarNota(inscripcion, nuevaNota):
	Inscripcion.setNota(inscripcion, nuevaNota)

def eliminarNota(inscripcion):
	Inscripcion.setNota(inscripcion, -1)