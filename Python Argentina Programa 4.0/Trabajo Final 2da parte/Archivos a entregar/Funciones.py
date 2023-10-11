from Encargado import Encargado
from Profesor import Profesor
from Inscripcion import Inscripcion
import tkinter.simpledialog as sd
import tkinter.messagebox as mb

dicProfesores = {}
dicEncargados = {}
dicInscripciones = {}

# Carga los datos de los archivos de texto en los diccionarios correspondientes

def cargarProfesores():																				
	archivo = open("Trabajo Final 2da parte/Archivos a entregar/Profesores.txt", "r")
	texto = archivo.readlines()																		
	archivo.close()																					

	for linea in texto:
		linea = linea.rstrip("\n")
		lineaString = linea.split(",")
		dicProfesores[lineaString[0] + lineaString[1]] =  Profesor(lineaString[0], lineaString[1], lineaString[2], lineaString[3])

def cargarEncargados():																				
	archivo = open("Trabajo Final 2da parte/Archivos a entregar/Encargados.txt", "r")															#la institucion y cargo los datos
	texto = archivo.readlines()																		
	archivo.close()																					

	for linea in texto:
		linea = linea.rstrip("\n")
		lineaString = linea.split(",")
		dicEncargados[lineaString[0] + lineaString[1]] = Encargado(lineaString[0], lineaString[1])

def cargarInscripciones():
	try:																			
		archivo = open("Trabajo Final 2da parte/Archivos a entregar/Inscripciones.txt", "r")														#y almacena los datos en un
		texto = archivo.readlines()																		
		archivo.close()																					
		dicInscripciones.clear()																		
		for linea in texto:
			linea = linea.rstrip("\n")
			listaString = linea.split(",")
			dicInscripciones[listaString[0] + listaString[1] + listaString[2]] = Inscripcion(listaString[0], listaString[1],\
			listaString[2], listaString[3], listaString[4], listaString[5], listaString[6])
	except FileNotFoundError:
		archivo = open("Trabajo Final 2da parte/Archivos a entregar/Inscripciones.txt", "w")
		archivo.close()

# Actualiza el archivo de texto 'Inscripciones' segun los cambios hechos sobre el diccionario de inscripciones

def actualizarInsEnTXT():
	archivo = open("Trabajo Final 2da parte/Archivos a entregar/Inscripciones.txt", "w")
											
	for inscripcion in dicInscripciones.values():						
		archivo.write(str(inscripcion))	
		archivo.write("\n")

	archivo.close()

def actTXTCargarDic():
	actualizarInsEnTXT()
	cargarInscripciones()

# Valida un profesor o encargado segun su clave

def validarProfesor(clave):									
	return (clave in dicProfesores.keys())					

def validarEncargado(clave):								
	return (clave in dicEncargados.keys())					
															
# Valida un DNI, una fecha, una nota y una inscripcion
def validarDNI(DNI):																			
	return(7 <= len(str(DNI)) <= 8)								

def validarFecha(fecha):									
	aRet = False											
	if(fecha != None):
		listaString = fecha.split("/")							
		try:
			if( (1 <= len(listaString[0]) <= 2) and (listaString[0].isdigit()) and (0 < int(listaString[0]) <= 31) and \
				(len(listaString[1]) == 2) and (listaString[1].isdigit()) and (0 < int(listaString[1]) <= 12) and \
				(len(listaString[2]) == 2) and (listaString[2].isdigit()) and (0 < int(listaString[2])) ):
				aRet = True
		except IndexError:
			aRet = False
	return aRet
	
def validarNota(nota):
	return (0 <= nota <= 10)

def validarInscripcion(clave):
	return (dicInscripciones[clave] in dicInscripciones.values())

# Pregunto los datos necesarios para validar una inscripcion

def preguntarClave():
	fecha = sd.askstring("Ingresar datos", "Ingrese la fecha de la inscripcion:")
	alumno = sd.askstring("Ingresar datos", "Ingrese el nombre del alumno de la inscripcion:")
	materia = sd.askstring("Ingresar datos", "Ingrese la materia de la inscripcion:")
	if(fecha == None or alumno == None or materia == None):
		mb.showerror("Error", "No se ingresaron todos los datos")
	else:
		if(validarFecha(fecha)):
			return fecha + alumno + materia
		else:
			mb.showerror("Error", "Fecha invalida")

# Preguntos los datos necesarios para crear una nueva inscripcion

def preguntarDatos():
	fecha = sd.askstring("Ingresar datos", "Ingrese la fecha de la nueva inscripcion:")
	alumno = sd.askstring("Ingresar datos", "Ingrese el nombre del alumno de la nueva inscripcion:")
	materia = sd.askstring("Ingresar datos", "Ingrese la materia de la nueva inscripcion:")
	profesor = sd.askstring("Ingresar datos", "Ingrese el profesor de la nueva inscripcion:")
	curso = sd.askinteger("Ingresar datos", "Ingrese el curso de la nueva inscripcion:")
	division = sd.askstring("Ingresar datos", "Ingrese la division de la nueva inscripcion:")
	if(fecha == None or alumno == None or materia == None or profesor == None or curso == None or division == None):
		mb.showerror("Error", "No se ingresaron todos los datos")
	else:
		if(not validarFecha(fecha)):
			mb.showerror("Error", "Fecha invalida")
		else:
			return fecha, alumno, materia, profesor, curso, division
	return None, None, None, None, None, None