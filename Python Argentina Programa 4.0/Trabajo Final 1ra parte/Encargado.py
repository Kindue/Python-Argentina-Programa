######################### ENCARGADO #########################
#Modela a un encargado para el sistema. Un encargado puede crear y eliminar inscripciones
#Ademas puede modificar cualquier dato de una inscripcion excepto su nota

import Inscripcion

def incorporarInscripcion(inscripcion):
	archivo = open("Inscripciones.txt", "a")
	archivo.write("\n")
	archivo.write(Inscripcion.toString(inscripcion))
	archivo.close()

def eliminarInscripcion(inscripcion):
	archivo = open("Inscripciones.txt",  "r")
	texto = archivo.readlines()
	archivo.close()

	archivo = open("Inscripciones.txt", "w")
	for linea in texto:
		if(linea.strip("\n") != Inscripcion.toString(inscripcion)):
			archivo.write(linea)
	archivo.close()

def modificarEnArchivo(inscripcionVieja, insModificada):
	archivo = open("Inscripciones.txt", "r")
	texto = archivo.readlines()
	archivo.close()

	archivo = open("Inscripciones.txt", "w")
	for linea in texto:
		if(linea.strip("\n") == inscripcionVieja):
			archivo.write(insModificada)
		else:
			archivo.write(linea)

def validarEncargado(nombre, dni):
	archivo = open("Encargados.txt", "r")
	texto = archivo.readlines()
	archivo.close()
	
	for linea in texto:
		listaStrings = linea.split(",")
		if(listaStrings[0].upper() == nombre.upper() and listaStrings[1] == str(dni)):
			return True
	return False


def modificarFecha(inscripcion, nuevaFecha):
	insAux = Inscripcion.toString(inscripcion)
	setFecha(inscripcion, nuevaFecha)
	modificarEnArchivo(insAux, Inscripcion.toString(inscripcion))

def modificarAlumno(inscripcion, nuevoAlumno):
	insAux = Inscripcion.toString(inscripcion)
	setAlumno(inscripcion, nuevoAlumno)
	modificarEnArchivo(insAux, Inscripcion.toString(inscripcion))

def modificarMateria(inscripcion, nuevaMateria):
	insAux = Inscripcion.toString(inscripcion)
	setMateria(inscripcion, nuevaMateria)
	modificarEnArchivo(insAux, Inscripcion.toString(inscripcion))

def modificarProfesor(inscripcion, nuevoProfesor):
	insAux = Inscripcion.toString(inscripcion)
	setProfesor(inscripcion, nuevoProfesor)
	modificarEnArchivo(insAux, Inscripcion.toString(inscripcion))

def modificarCurso(inscripcion, nuevoCurso):
	insAux = Inscripcion.toString(inscripcion)
	setCurso(inscripcion, nuevoCurso)
	modificarEnArchivo(insAux, Inscripcion.toString(inscripcion))

def modificarDivision(inscripcion, nuevaDivision):
	insAux = Inscripcion.toString(inscripcion)
	setDivision(inscripcion, nuevaDivision)
	modificarEnArchivo(insAux, Inscripcion.toString(inscripcion))

nuevaINS = crearInscripcion("24", "Juan", "Matematica", "Jose", 4, 5)
print(toString(nuevaINS))
incorporarInscripcion(nuevaINS)

nuevaINS2 = crearInscripcion("65", "Pedro", "Lengua", "Fernando", 2, 1)
print(toString(nuevaINS2))
incorporarInscripcion(nuevaINS2)

eliminarInscripcion(nuevaINS)
modificarFecha(nuevaINS2, "90")
print(toString(nuevaINS2))
modificarAlumno(nuevaINS2, "Martin")
print(toString(nuevaINS2))

