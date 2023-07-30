######################### INSCRIPCION #########################
#Modela una inscripcion para un examen, contiene consultas triviales
#para obtener y modificar sus atributos los cuales son:
#fecha, nombre del alumno, nombre de la materia, nombre del profesor
#curso, division y nota

def crearInscripcion(fecha, alumno, materia, profesor, curso, division):
	return {"fecha": fecha, "alumno": alumno, "materia": materia, "profesor": profesor, \
	"curso": str(curso), "division": str(division), "nota": "-1"}

def toString(inscripcion):
	return (inscripcion["fecha"] + "," + inscripcion["alumno"] + "," + inscripcion["materia"] + "," +\
		inscripcion["profesor"] + "," + inscripcion["curso"] + "," + inscripcion["division"] + "," + inscripcion["nota"])

def getFecha(inscripcion):
	return inscripcion["fecha"]

	def getAlumno(inscripcion):
	return inscripcion["alumno"]

	def getMateria(inscripcion):
	return inscripcion["materia"]

	def getProfesor(inscripcion):
	return inscripcion["profesor"]

	def getCurso(inscripcion):
	return inscripcion["Curso"]

	def getDivision(inscripcion):
	return inscripcion["division"]

	def getNota(inscripcion):
	return inscripcion["nota"]

def setFecha(inscripcion, nuevaFecha):
	inscripcion["fecha"] = nuevaFecha

def setAlumno(inscripcion, nuevoAlumno):
	inscripcion["alumno"] = nuevoAlumno

def setMateria(inscripcion, nuevaMateria):
	inscripcion["materia"] = nuevaMateria

def setProfesor(inscripcion, nuevoProfesor):
	inscripcion["profesor"] = nuevoProfesor

def setCurso(inscripcion, nuevoCurso):
	inscripcion["curso"] = nuevoCurso

def setDivision(inscripcion, nuevaDivision):
	inscripcion["division"] = nuevaDivision

def setNota(inscripcion, nuevaNota):
	inscripcion["nota"] = nuevaNota