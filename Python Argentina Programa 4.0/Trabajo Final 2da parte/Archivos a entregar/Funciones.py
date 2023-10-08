from Encargado import Encargado
from Profesor import Profesor
from Inscripcion import Inscripcion
import os
import time

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
	archivo = open("Trabajo Final 2da parte/Archivos a entregar/Profesores.txt", "r")															#la institucion y cargo los datos
	texto = archivo.readlines()																		#en un diccionario de profesores
	archivo.close()																					#para facilitar la validacion

	for linea in texto:
		linea = linea.rstrip("\n")
		lineaString = linea.split(",")
		dicEncargados[lineaString[0] + lineaString[1]] = Encargado(lineaString[0], lineaString[1])

def cargarInscripciones():
	try:																			#Lee el archivo creado por el programa
		archivo = open("Inscripciones.txt", "r")														#y almacena los datos en un
		texto = archivo.readlines()																		#diccionario de inscripciones
		archivo.close()																					#que sera modificado durante la
		dicInscripciones.clear()																		#ejecucion del programa principal
		for linea in texto:
			linea = linea.rstrip("\n")
			listaString = linea.split(",")
			dicInscripciones[listaString[0] + listaString[1] + listaString[2]] = Inscripcion(listaString[0], listaString[1],\
			listaString[2], listaString[3], listaString[4], listaString[5], listaString[6])
	except FileNotFoundError:
		archivo = open("Inscripciones.txt", "w")
		archivo.close()

def actualizarInsEnTXT():												#Actualiza el archivo de texto 'Inscripciones'
	archivo = open("Inscripciones.txt", "w")							#segun los cambios hechos sobre el diccionario
																		#de inscripciones
	for inscripcion in dicInscripciones.values():						#Junto con la carga de inscripciones, el archivo TXT se
		archivo.write(str(inscripcion))									#actualiza cada vez que el usuario vuelve hacia atras en un menu
		archivo.write("\n")

	archivo.close()

def validarProfesor(clave):									#Valida un profesor chequeando
	aRet = False											#si pertenece al diccionario
	if(clave in dicProfesores.keys()):						#de profesores
		aRet = True
	else:
		print("Error, no existe un profesor con los datos ingresados")
	return aRet 

def validarEncargado(clave):								#Valida un encargado chequeando
	aRet = False											#si pertenece al diccionario
	if(clave in dicEncargados.keys()):						#de encargados
		aRet = True
	else:
		print("Error, no existe un encargado con los datos ingresados")
	return aRet

def validarDNI(DNI):										#Valida un DNI chequeando										#si el DNI tiene 7 u 8
	return(7 <= len(DNI) <= 8)								#si el DNI tiene 7 u 8 numeros

def validarFecha(fecha):									#Valida una fecha chequeando que la fecha tenga
	aRet = False											#1 o 2 numeros del 1 al 31 para el dia
	listaString = fecha.split("/")							#2 numeros del 1 al 12 para el mes y 2 numeros para el año
	try:
		if( (1 <= len(listaString[0]) <= 2) and (listaString[0].isdigit()) and (0 < int(listaString[0]) <= 31) and \
			(len(listaString[1]) == 2) and (listaString[1].isdigit()) and (0 < int(listaString[1]) <= 12) and \
			(len(listaString[2]) == 2) and (listaString[2].isdigit()) and (0 < int(listaString[2])) ):
			aRet = True
		else:
			print("Error, fecha invalida")
	except IndexError:
		aRet = False
	finally:
		return aRet