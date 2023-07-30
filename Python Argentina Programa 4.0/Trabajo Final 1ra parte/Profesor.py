######################### PROFESOR #########################
#Modela a un profesor en el sistema. Un profesor puede modificar las notas
#de los alumnos en las inscripciones y ademas puede eliminar inscripciones

import Inscripcion

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

def validarProfesor(nombre, materia, curso, division):
	archivo = open("Profesores.txt", "r")
	texto = archivo.readlines()
	archivo.close()

	for linea in texto:
		listaStrings = linea.split(",")
		if(listaStrings[0].upper() == nombre.upper() and listaStrings[1].upper() == materia.upper()\
		 and listaStrings[2] == str(curso) and listaStrings[3] == str(division)):
			return True
	return False

def modificarNota(inscripcion, nuevaNota):
	insAux = Inscripcion.toString(inscripcion)
	setNota(inscripcion, nuevaNota)
	modificarEnArchivo(insAux, Inscripcion.toString(inscripcion))