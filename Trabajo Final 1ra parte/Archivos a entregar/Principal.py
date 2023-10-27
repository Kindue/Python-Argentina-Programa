######################### PROGRAMA PRINCIPAL #########################
#El programa principal se ocupa de mostrar los menus para los profesores
#y los encargados, modificar los datos de las inscripciones y
#cargar y leer los datos de las inscripciones en un archivo de texto.
#Cada vez que el usuario vuelve al menu principal se cargan los datos al
#diccionario de inscripciones local para que puedan ser modificados por
#un profesor o un encargado sin salir del programa.
#Cuando se sale del programa estos datos son cargados al archivo de texto
#'Inscripciones' creado en el mismo directorio del programa
#Los archivos de texto 'Profesores' y 'Encargados' deben estar en el mismo
#directorio que el programa para que funcione correctamente.

import Encargado
import Profesor
import os
import time

dicProfesores = {}
dicEncargados = {}
dicInscripciones = {}

########## FUNCIONES PARA EL PROGRAMA PRINCIPAL ##########

def limpiar_pantalla():						#Limpia la pantalla de la consola
    if os.name == 'nt':  					# En caso de que el programa sea utilizado en Windows
        os.system('cls')
    else:  									# En caso de que el programa sea utilizado en UNIX (Linux y macOS)
        os.system('clear')

def cargarProfesores():																				#Lee el archivo proporcionado por 
	archivo = open("Profesores.txt", "r")															#la institucion y cargo los datos
	texto = archivo.readlines()																		#en un diccionario de profesores
	archivo.close()																					#para ayudar la validacion

	for linea in texto:
		linea = linea.rstrip("\n")
		lineaString = linea.split(",")
		dicProfesores[lineaString[0] + lineaString[1]] = Profesor.crearProfesor(lineaString[0],\
		 lineaString[1], lineaString[2], lineaString[3])

def cargarEncargados():																				#Lee el archivo proporcionado por
	archivo = open("Encargados.txt", "r")															#la institucion y cargo los datos
	texto = archivo.readlines()																		#en un diccionario de profesores
	archivo.close()																					#para facilitar la validacion

	for linea in texto:
		linea = linea.rstrip("\n")
		lineaString = linea.split(",")
		dicEncargados[lineaString[1]] = Encargado.crearEncargado(lineaString[0], lineaString[1])

def cargarInscripciones():																			#Lee el archivo creado por el programa
	archivo = open("Inscripciones.txt", "r")														#y almacena los datos en un
	texto = archivo.readlines()																		#diccionario de inscripciones
	archivo.close()																					#que sera modificado durante la
	dicInscripciones.clear()																		#ejecucion del programa principal
	for linea in texto:
		linea = linea.rstrip("\n")
		listaString = linea.split(",")
		Encargado.incorporarInscripcion(listaString[0], listaString[1], listaString[2], listaString[3],\
		 listaString[4], listaString[5], dicInscripciones)

def toString(inscripcion):			#Convierte una inscripcion a un string con el formato de una inscripcion en el archivo de texto creado por el programa
	return (str(inscripcion["fecha"]) + "," + inscripcion["alumno"] + "," + inscripcion["materia"] + "," + inscripcion["profesor"] + "," + str(inscripcion["curso"]) + "," + str(inscripcion["division"]) + "," + str(inscripcion["nota"]))											#inscripcion en el archivo de texto

def actualizarInsEnTXT():												#Actualiza el archivo de texto 'Inscripciones'
	archivo = open("Inscripciones.txt", "w")							#segun los cambios hechos sobre el diccionario
																		#de inscripciones
	for inscripcion in dicInscripciones.values():						#Junto con la carga de inscripciones, el archivo TXT se
		archivo.write(toString(inscripcion))							#actualiza cada vez que el usuario vuelve hacia atras en un menu
		archivo.write("\n")

	archivo.close()

def validarProfesor(clave):									#Valida un profesor chequeando
	aRet = False											#si pertenece al diccionario
	if(clave in dicProfesores.keys()):						#de profesores
		aRet = True
	else:
		print("Error, no existe un profesor con los datos ingresados")
	return aRet 

def validarEncargado(DNI):									#Valida un encargado chequeando
	aRet = False											#si pertenece al diccionario
	if(str(DNI) in dicEncargados.keys()):					#de encargados
		aRet = True
	else:
		print("Error, no existe un encargado con los datos ingresados")
	return aRet

def validarDNI(DNI):										#Valida un DNI chequeando
	aRet = False											#si el DNI tiene 7 u 8
	if(7 <= len(DNI) <= 8):									#numeros
		aRet = True
	return aRet

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

def cargarArchivos():
	aRet = False
	print("BIENVENIDO AL SISTEMA DE INSCRIPCIONES")							#Reviso que los archivos de profesores y encargados
	print("--"*40)															#esten en el mismo directorio que el programa principal
	print("CARGANDO PROFESORES, ENCARGADOS E INSCRIPCIONES")				#Si no lo estan, lanzo un error. Si estan entonces cargo
	print("--"*40)															#las inscripciones.
	try:
		cargarProfesores()
		cargarEncargados()
		time.sleep(1)
		limpiar_pantalla()
	except FileNotFoundError:
		print("Error, no se encontraron los archivos 'Profesores.txt' y 'Encargados.txt'")
		print("en el mismo directorio del programa!")
		print("Vuelva a iniciar el programa luego de que los archivos mencionados")
		print("se ubiquen en la misma carpeta que el programa principal!")
		print("Presiones 'ENTER' para salir")
		input()
	else:
		try:
			cargarInscripciones()													#Si es la primera vez que se ejecuta el programa, el
		except FileNotFoundError:													#archivo de inscripciones se crea. Si no, se cargan
			archivo = open("Inscripciones.txt", "w")								#las inscripciones del archivo en un diccionario
			archivo.close()
		finally:
			aRet = True
	return aRet

def mPrincipal():
	print("INGRESE EL NUMERO DE LA OPCION QUE DESEE UTILIZAR: ")					#Menu principal que permite elegir entre profesores
	print("--"*40)																	#o encargados
	print("--"*40)
	print("1 : MENU PARA ENCARGADOS")
	print("--"*40)
	print("2 : MENU PARA PROFESORES")
	print("--"*40)
	print("0 : SALIR")
	print("--"*40)
	opcion = input()
	limpiar_pantalla()
	return opcion

def mEncargados():
	print("A CONTINUACION INGRESE LA OPCION QUE DESEE UTILIZAR")					#Menu de encargados luego de ser verificado
	print("--"*40)																	#el encargado que se ingreso				
	print("--"*40)
	print("1 : CREAR UNA INSCRIPCION")
	print("--"*40)
	print("2 : MODIFICAR UNA INSCRIPCION")
	print("--"*40)
	print("3 : ELIMINAR UNA INSCRIPCION")
	print("--"*40)
	print("0 : VOLVER AL MENU PRINCIPAL")
	print("--"*40)
	opcion = input()
	limpiar_pantalla()
	return opcion

def mEncModif():																		#Menu para la modificacion de inscripciones
	print("--"*40)																		#utilizado solo por encargados
	print("INGRESE LA OPCION DE LO QUE DESEE MODIFICAR EN LA INSCRIPCION INGRESADA:")
	print("--"*40)
	print("--"*40)
	print("1 : Fecha en la inscripcion")
	print("--"*40)
	print("2 : Nombre del alumno en la inscripcion")
	print("--"*40)
	print("3 : Nombre de la materia en la inscripcion")
	print("--"*40)
	print("4 : Nombre del profesor en la inscripcion")
	print("--"*40)
	print("5 : Curso en la inscripcion")
	print("--"*40)
	print("6 : Division en la inscripcion")
	print("--"*40)
	print("0 : Volver al menu de encargados")
	print("--"*40)
	opcion = input()
	limpiar_pantalla()
	return opcion

def mProfesores():															#Menu de profesores luego de ser verificado
	limpiar_pantalla()														#el profesor que se ingreso
	print("A CONTINUACION INGRESE LA OPCION QUE DESEE UTILIZAR")
	print("--"*40)
	print("--"*40)
	print("1 : MODIFICAR UNA NOTA")
	print("--"*40)
	print("2 : ELIMINAR UNA NOTA")
	print("--"*40)
	print("0 : VOLVER AL MENU PRINCIPAL")
	print("--"*40)
	opcion = input()
	limpiar_pantalla()
	return opcion

def mVerificacionEncargados():
	loopEncargado = True
	while(loopEncargado):
		print("ENCARGADOS")										#Valida a un encargado primero revisando que su DNI sea valido
		print("--"*40)											#y luego revisando el DNI en las claves del diccionario
		print("Ingrese su DNI:")								#de encargados
		DNI = input()
		if(validarDNI(DNI) and validarEncargado(DNI)):
			limpiar_pantalla()
			print("--"*40)
			print("INGRESO EXITOSO")
			loopEncargado = False
			return True
		else:
			print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu principal")
			opAux = input()
			if(opAux == '0'):
				print("Volviendo al menu principal")
				time.sleep(1)
				loopEncargado = False
			limpiar_pantalla()

def mVerficacionProfesores():
	loopProfesor = True
	while(loopProfesor):															#Si la opcion en el menu principal fue un 2 ingreso																		#a la validacion de profesores
		limpiar_pantalla()															#Un profesor se valida con una clave de tipo string
		print("PROFESORES")															#formada por su nombre concatenada con la materia que dicta
		print("--"*40)
		print("Ingrese su nombre:")
		nombre = input()
		print("Ingrese la materia que dicta:")
		materia = input()
		if(validarProfesor(nombre+materia)):
			loopProfesor = False
			print("--"*40)
			print("INGRESO EXITOSO")
			print("--"*40)
			time.sleep(1)
			return True
		else:
			print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu principal")
			opAux = input()
			if(opAux == '0'):
				loopProfesor = False
				print("Volviendo al menu principal")
			print("--"*40)
			time.sleep(1)
	limpiar_pantalla()

def cInscripcion():																	#Crea una nueva inscripcion si los datos ingresados
	loopOpEncargado = True															#son correctos
	while(loopOpEncargado):											
		print("Ingrese la fecha de la nueva inscripcion con el formato DD/MM/YY:")
		fecha = input()
		print("Ingrese el nombre del alumno de la nueva inscripcion:")
		alumno = input()
		print("Ingrese el nombre de la materia de la nueva inscripcion:")
		materia = input()
		print("Ingrese el nombre del profesor de la nueva inscripcion:")
		profesor = input()
		print("Ingrese el curso de la nueva inscripcion:")					#Los cursos y divisiones deben ser numeros
		curso = int(input())
		print("Ingrese la division de la nueva inscripcion")
		division = int(input())
		limpiar_pantalla()
		if(validarFecha(fecha)):											#Si la fecha ingresada es valida, consulto si la inscripcion
			if((fecha+alumno+materia) not in dicInscripciones.keys()):		#existe o no en el diccionario de inscripciones											
				Encargado.incorporarInscripcion(fecha, alumno, materia, profesor, curso, division, dicInscripciones)
				print("Incorporacion de inscripcion exitosa! Volviendo al menu anterior") 				#Si no existe almaceno una nueva
			else:																						#inscripcion
				print("Error, inscripcion ya almacenada")
				print("volviendo al menu de encargados en caso de que desee modificarla")
			loopOpEncargado = False
			time.sleep(1)
		else:
			print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu anterior")
			opEncargado = input()
			if(opEncargado == '0'):
				loopOpEncargado = False
				print("Volviendo al menu anterior")
				time.sleep(1)
		limpiar_pantalla()

def mValidarIns():															#Valido una inscripcion para su modificacion o eliminacion
	loopOpEncargado = True													#Esto es utilizado en los menus de profesores y encargados
	claveInscripcion = ''
	while(loopOpEncargado):																				
		print("Ingrese la fecha de la inscripcion que desee modificar con el formato DD/MM/YY:")
		fecha = input()
		print("Ingrese el nombre del alumno en la inscripcion que desee modificar:")
		alumno = input()
		print("Ingrese el nombre de la materia en la inscripcion que desee modificar:")
		materia = input()
		print("--"*40)
		if(fecha+alumno+materia in dicInscripciones.keys() and validarFecha(fecha)):
			print("Inscripcion valida!")
			claveInscripcion = fecha+alumno+materia
			loopOpEncargado = False
			time.sleep(1)
		else:
			if(fecha+alumno+materia not in dicInscripciones.keys()):
				limpiar_pantalla()																	#ingresados
				print("Error, la inscripcion ingresada no pertenece al sistema")
			print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu anterior")
			opEncargado = input()
			if(opEncargado == '0'):
				loopOpEncargado = False
				print("Volviendo al menu de anterior")
			print("--"*40)
		limpiar_pantalla()
	return claveInscripcion

def modFecha(claveInscripcion):														#Modifico la fecha en una inscripcion
	loopOpModificacion = True														#ingresada y validada anteriormente
	while(loopOpModificacion):														#Esta tarea se realiza desde el menu de encargados
		print("Ingrese una nueva fecha para modificar la inscripcion ingresada anteriormente con el formato DD/MM/YY:")
		nuevaFecha = input()
		if(validarFecha(nuevaFecha)):
			limpiar_pantalla()
			Encargado.modificarFecha(dicInscripciones[claveInscripcion], nuevaFecha)
			print("Fecha en la inscripcion modificada con exito!")
			print("--"*40)
			loopOpModificacion = False
			time.sleep(1)
		else:
			print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu de modificacion de inscripcion")
			opEncargado = input()
			if(opEncargado == '0'):
				loopOpModificacion = False
			print("--"*40)
		limpiar_pantalla()

def modAlumno(claveInscripcion):												#Modifico el nombre de un alumno en una inscripcion
	limpiar_pantalla()															#ingresada y validada anteriormente
	print("Ingrese el nuevo nombre del alumno para modificar la inscripcion ingresada anteriormente:")
	nuevoAlumno = input()
	print("--"*40)																#Esta tarea se realiza desde el menu de encargados
	limpiar_pantalla()
	Encargado.modificarAlumno(dicInscripciones[claveInscripcion], nuevoAlumno)
	print("Nombre del alumno en la inscripcion modificado con exito!")
	print("--"*40)
	time.sleep(1)
	limpiar_pantalla()

def modMateria(claveInscripcion):												#Modifico la materia en una inscripcion
	limpiar_pantalla()															#ingresada y validada anteriormente
	print("Ingrese la nueva materia para modificar la inscripcion ingresada anteriormente:")
	nuevaMateria = input()
	print("--"*40)																#Esta tarea se realiza desde el menu de encargados
	limpiar_pantalla()
	Encargado.modificarMateria(dicInscripciones[claveInscripcion], nuevaMateria)
	print("Materia en la inscripcion modificada con exito!")
	print("--"*40)
	time.sleep(1)
	limpiar_pantalla()

def modProfesor(claveInscripcion):												#Modifico el profesor en una inscripcion
	limpiar_pantalla()															#ingresada y validada anteriormente
	print("Ingrese el nuevo nombre del profesor para modificar la inscripcion ingresada anteriormente:")
	nuevoProfesor = input()
	print("--"*40)																#Esta tarea se realiza desde el menu de encargados
	limpiar_pantalla()
	Encargado.modificarProfesor(dicInscripciones[claveInscripcion], nuevoProfesor)
	print("Nombre del profesor en la inscripcion modificado con exito!")
	print("--"*40)
	time.sleep(1)
	limpiar_pantalla()

def modCurso(claveInscripcion):													#Modifico el curso en una inscripcion
	loopOpModificacion = True													#ingresada y validada anteriormente
	while(loopOpModificacion):													#Esta tarea se realiza desde el menu de encargados
		try:																	#Los cursos y divisiones solo pueden ser numeros
			limpiar_pantalla()
			print("Ingrese el nuevo numero de curso para modificar la inscripcion ingresada anteriormente:")
			nuevoCurso = int(input())
			print("--"*40)
		except ValueError:
			limpiar_pantalla()
			print("Error, curso no valido!")
			print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu de modificacion de inscripcion")
			opEncargado = input()
			if(opEncargado == '0'):
				loopOpModificacion = False
			print("--"*40)
		else:
			limpiar_pantalla()
			Encargado.modificarCurso(dicInscripciones[claveInscripcion], nuevoCurso)
			print("Curso en la inscripcion modificado con exito!")
			loopOpModificacion = False
			print("--"*40)
		time.sleep(1)
		limpiar_pantalla()

def modDivision(claveInscripcion):														#Modifico la division en una inscripcion
	loopOpModificacion = True															#ingresada y validada anteriormente
	while(loopOpModificacion):															#Esta tarea se realiza desde el menu de encargados
		try:
			limpiar_pantalla()
			print("Ingrese el nuevo numero de division para modificar la inscripcion ingresada anteriormente:")
			nuevaDivision = int(input())
			print("--"*40)
		except ValueError:
			limpiar_pantalla()
			print("Error, division no valida!")
			print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu de modificacion de inscripcion")
			opEncargado = input()
			if(opEncargado == '0'):
				loopOpModificacion = False
			print("--"*40)
		else:
			limpiar_pantalla()
			Encargado.modificarDivision(dicInscripciones[claveInscripcion], nuevaDivision)
			print("Division en la inscripcion modificada con exito!")
			loopOpModificacion = False
			print("--"*40)
		time.sleep(1)
		limpiar_pantalla()

def modNota(claveInscripcion):
	loopOpModificacion = True											#Modifico la nota en una inscripcion
	while(loopOpModificacion):											#ingresada y validada anteriormente
		limpiar_pantalla()												#Esta tarea se realiza desde el menu de profesores
		try:
			print("Ingrese la nueva nota de la inscripcion ingresada anteriormente:")
			nuevaNota = int(input())
			if(0 <= nuevaNota > 10):									#La nota debe ser mayor que 0 y menor o igual a 10
				raise Exception
		except ValueError:
			limpiar_pantalla()
			print("Error, nota no valida!")
			print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu de modificacion de inscripcion")
			opEncargado = input()
			if(opEncargado == '0'):
				loopOpModificacion = False
			print("--"*40)
		except Exception:
			limpiar_pantalla()
			print("Error, la nota debe ser un numero del 1 al 10!")
			print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu de modificacion de inscripcion")
			opEncargado = input()
			if(opEncargado == '0'):
				loopOpModificacion = False
			print("--"*40)
		else:
			limpiar_pantalla()											#Si la nota es valida, modifico la nota de la inscripcion en el diccionario
			Profesor.modificarNota(dicInscripciones[claveInscripcion], nuevaNota)
			print("Nota en la inscripcion ingresada modificada con exito!")
			loopOpModificacion = False
		time.sleep(1)
		limpiar_pantalla()

def eInscripcion():
	loopOpEncargado = True
	while(loopOpEncargado):																#Pido los datos de una inscripcion																	#y los valido
		limpiar_pantalla()
		print("Ingrese la fecha de la inscripcion que desee eliminar con el formato DD/MM/YY:")
		fecha = input()
		print("Ingrese el nombre del alumno en la inscripcion que desee eliminar:")
		alumno = input()
		print("Ingrese el nombre de la materia en la inscripcion que desee eliminar:")
		materia = input()
		print("--"*40)
		if(validarFecha(fecha)):
			limpiar_pantalla()
			if(fecha+alumno+materia in dicInscripciones.keys()):											#Si hay una inscripcion con los datos
				Encargado.eliminarInscripcion(dicInscripciones[fecha+alumno+materia], dicInscripciones) 	#ingresados la elimino
				print("La inscripcion ingresada fue eliminada con exito! volviendo al menu de encargados")
			else:																							#Si no la hay muestro un mensaje de error
				print("Error, la inscripcion ingresada no pertenece al sistema")
				print("Volviendo al menu de encargados")
			loopOpEncargado = False
			print("--"*40)
			time.sleep(1)
		else:
			print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu de encargados")
			opEncargado = input()
			if(opEncargado == '0'):
				loopOpEncargado = False
			print("--"*40)
		limpiar_pantalla()

def eNota(claveInscripcion):														#Elimino una nota, insertando un '-1' en el campo
	Profesor.eliminarNota(dicInscripciones[claveInscripcion])						#de la nota de la inscripcion ingresada anteriormente
	print("La nota de la inscripcion ingresada fue eliminada con exito! Volviendo al menu de profesores")
	time.sleep(1)
	limpiar_pantalla()


########## PROGRAMA PRINCIPAL ##########

if(cargarArchivos()):
	loopPrincipal = True
	while(loopPrincipal):
		opcionPrincipal = mPrincipal()
		if(opcionPrincipal == '1'):	
			ingreso = mVerificacionEncargados()
			if(ingreso):						
				loopMenuEncargado = True
				while(loopMenuEncargado):																				
					opcionEncargado = mEncargados()
					if(opcionEncargado == '1'):										
						cInscripcion()
					elif(opcionEncargado == '2'):	
						inscripcionAModificar = mValidarIns()
						if(inscripcionAModificar != ''):
							loopOpEncargado = True
							while(loopOpEncargado):
								opEncargadoMod = mEncModif()
								if(opEncargadoMod == '1'):
									modFecha(inscripcionAModificar)
								elif(opEncargadoMod == '2'):
									modAlumno(inscripcionAModificar)
								elif(opEncargadoMod == '3'):
									modMateria(inscripcionAModificar)
								elif(opEncargadoMod == '4'):
									modProfesor(inscripcionAModificar)
								elif(opEncargadoMod == '5'):
									modCurso(inscripcionAModificar)
								elif(opEncargadoMod == '6'):
									modDivision(inscripcionAModificar)
								elif(opEncargadoMod == '0'):
									limpiar_pantalla()		
									print("Volviendo al menu de encargados!")
									actualizarInsEnTXT()
									cargarInscripciones()
									loopOpEncargado = False
									print("--"*40)
									time.sleep(1)
								else:
									limpiar_pantalla()
									print("Error al ingresar una opcion valida, intente de nuevo!")
									print("--"*40)
									time.sleep(1)
					elif(opcionEncargado == '3'):	
						eInscripcion()
					elif(opcionEncargado == '0'):
						limpiar_pantalla()	
						print("Volviendo al menu principal!")
						loopMenuEncargado = False
						actualizarInsEnTXT()
						cargarInscripciones()
						print("--"*40)
						time.sleep(1)
					else:
						limpiar_pantalla()
						print("Error al ingresar una opcion valida, intente de nuevo!")	
						time.sleep(1)
		elif(opcionPrincipal == '2'):
			ingreso = mVerficacionProfesores()
			if(ingreso):
				loopMenuProfesor = True
				while(loopMenuProfesor):
					opcionProfesor = mProfesores()	
					if(opcionProfesor == '1'):
						inscripcionAModificar = mValidarIns()
						if(inscripcionAModificar != ''):
							modNota(inscripcionAModificar)
					elif(opcionProfesor == '2'):
						inscripcionAEliminar = mValidarIns()
						if(inscripcionAEliminar != ''):
							eNota(inscripcionAEliminar)	
					elif(opcionProfesor == '0'):
						limpiar_pantalla()	
						print("Volviendo al menu principal!")
						loopMenuProfesor = False
						print("--"*40)
						actualizarInsEnTXT()
						cargarInscripciones()
						time.sleep(1)
					else:				
						limpiar_pantalla()	
						print("Error al ingresar una opcion valida, intente de nuevo!")
						print("--"*40)
						time.sleep(1)
		elif(opcionPrincipal == '0'):
			limpiar_pantalla()	
			print("GRACIAS POR UTILIZAR EL SISTEMA DE INSCRIPCIONES!")
			print("--"*40)
			actualizarInsEnTXT()
			loopPrincipal = False
			time.sleep(3)
		else:
			limpiar_pantalla()
			print("Error al ingresar una opcion valida, intente de nuevo!")
			print("--"*40)
			time.sleep(1)