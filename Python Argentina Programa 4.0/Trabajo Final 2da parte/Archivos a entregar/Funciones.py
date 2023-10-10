from Encargado import Encargado
from Profesor import Profesor
from Inscripcion import Inscripcion
import tkinter.simpledialog as sd
import tkinter.messagebox as mb

dicProfesores = {}
dicEncargados = {}
dicInscripciones = {}


def cargarProfesores():																				#Lee el archivo proporcionado por 
	archivo = open("Trabajo Final 2da parte/Archivos a entregar/Profesores.txt", "r")
	texto = archivo.readlines()																		#en un diccionario de profesores
	archivo.close()																					#para ayudar la validacion

	for linea in texto:
		linea = linea.rstrip("\n")
		lineaString = linea.split(",")
		dicProfesores[lineaString[0] + lineaString[1]] =  Profesor(lineaString[0], lineaString[1], lineaString[2], lineaString[3])

def cargarEncargados():																				#Lee el archivo proporcionado por
	archivo = open("Trabajo Final 2da parte/Archivos a entregar/Encargados.txt", "r")															#la institucion y cargo los datos
	texto = archivo.readlines()																		#en un diccionario de profesores
	archivo.close()																					#para facilitar la validacion

	for linea in texto:
		linea = linea.rstrip("\n")
		lineaString = linea.split(",")
		dicEncargados[lineaString[0] + lineaString[1]] = Encargado(lineaString[0], lineaString[1])

def cargarInscripciones():
	try:																			#Lee el archivo creado por el programa
		archivo = open("Trabajo Final 2da parte/Archivos a entregar/Inscripciones.txt", "r")														#y almacena los datos en un
		texto = archivo.readlines()																		#diccionario de inscripciones
		archivo.close()																					#que sera modificado durante la
		dicInscripciones.clear()																		#ejecucion del programa principal
		for linea in texto:
			linea = linea.rstrip("\n")
			listaString = linea.split(",")
			dicInscripciones[listaString[0] + listaString[1] + listaString[2]] = Inscripcion(listaString[0], listaString[1],\
			listaString[2], listaString[3], listaString[4], listaString[5], listaString[6])
	except FileNotFoundError:
		archivo = open("Trabajo Final 2da parte/Archivos a entregar/Inscripciones.txt", "w")
		archivo.close()

def actualizarInsEnTXT():												#Actualiza el archivo de texto 'Inscripciones'
	archivo = open("Trabajo Final 2da parte/Archivos a entregar/Inscripciones.txt", "w")							#segun los cambios hechos sobre el diccionario
																		#de inscripciones
	for inscripcion in dicInscripciones.values():						#Junto con la carga de inscripciones, el archivo TXT se
		archivo.write(str(inscripcion))									#actualiza cada vez que el usuario vuelve hacia atras en un menu
		archivo.write("\n")

	archivo.close()

def actTXTCargarDic():
	actualizarInsEnTXT()
	cargarInscripciones()

def validarProfesor(clave):									#Valida un profesor chequeando
	return (clave in dicProfesores.keys())					#si pertenece al diccionario
															#de profesores

def validarEncargado(clave):								#Valida un encargado chequeando
	return (clave in dicEncargados.keys())					#si pertenece al diccionario
															#de encargados

def validarDNI(DNI):										#Valida un DNI chequeando										#si el DNI tiene 7 u 8
	return(7 <= len(str(DNI)) <= 8)								#si el DNI tiene 7 u 8 numeros

def validarFecha(fecha):									#Valida una fecha chequeando que la fecha tenga
	aRet = False											#1 o 2 numeros del 1 al 31 para el dia
	if(fecha != None):
		listaString = fecha.split("/")							#2 numeros del 1 al 12 para el mes y 2 numeros para el año
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
	
def preguntarDatos():
	fecha = sd.askstring("Ingresar datos", "Ingrese la fecha de la nueva inscripcion:")
	alumno = sd.askstring("Ingresar datos", "Ingrese el nombre del alumno de la nueva inscripcion:")
	materia = sd.askstring("Ingresar datos", "Ingrese la materia de la nueva inscripcion:")
	profesor = sd.askstring("Ingresar datos", "Ingrese el profesor de la nueva inscripcion:")
	curso = sd.askinteger("Ingresar datos", "Ingrese el curso de la nueva inscripcion:")
	division = sd.askstring("Ingresar datos", "Ingrese la division de la nueva inscripcion:")
	if(fecha == None or alumno == None or materia == None or profesor == None or curso == None or division == None):
		mb.showerror("Error", "No se ingresaron todos los datos")
		return None, None, None, None, None, None
	else:
		if(not validarFecha(fecha)):
			mb.showerror("Error", "Fecha invalida")
		else:
			return fecha, alumno, materia, profesor, curso, division