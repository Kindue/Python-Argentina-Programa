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
																									#ejecucion del programa principal
	for linea in texto:
		linea = linea.rstrip("\n")
		listaString = linea.split(",")
		Encargado.incorporarInscripcion(listaString[0], listaString[1], listaString[2], listaString[3],\
		 listaString[4], listaString[5], dicInscripciones)

def toString(inscripcion):			#Convierte una inscripcion a un string con el formato de una inscripcion en el archivo de texto creado por el programa
	return (str(inscripcion["fecha"]) + "," + inscripcion["alumno"] + "," + inscripcion["materia"] + "," + inscripcion["profesor"] + "," + str(inscripcion["curso"]) + "," + str(inscripcion["division"]) + "," + str(inscripcion["nota"]))											#inscripcion en el archivo de texto

def actualizarInscripciones():											#Actualiza el archivo de texto 'Inscripciones'
	archivo = open("Inscripciones.txt", "w")							#segun los cambios hechos sobre el diccionario
																		#de inscripciones
	for inscripcion in dicInscripciones.values():
		archivo.write(toString(inscripcion))
		archivo.write("\n")

	archivo.close()

def validarProfesor(clave):									#Valida un profesor chequeando
	aRet = False											#si pertenece al diccionario
	if(clave in dicProfesores.keys()):						#de profesores
		aRet = True
	return aRet 

def validarEncargado(DNI):									#Valida un encargado chequeando
	aRet = False											#si pertenece al diccionario
	if(str(DNI) in dicEncargados.keys()):					#de encargados
		aRet = True
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
	except IndexError:
		aRet = False
	finally:
		return aRet

########## PROGRAMA PRINCIPAL ##########

print("BIENVENIDO AL SISTEMA DE INSCRIPCIONES")							
print("--"*40)
print("--"*40)
print("CARGANDO PROFESORES, ENCARGADOS E INSCRIPCIONES")
print("--"*40)
print("--"*40)
cargarProfesores()															#Presenta el menu principal y carga los diccionarios
cargarEncargados()															#de profesores y encargados
try:
	cargarInscripciones()													#Si es la primera vez que se ejecuta el programa, el
except FileNotFoundError:													#archivo de inscripciones se crea. Si no, se cargan
	archivo = open("Inscripciones.txt", "w")								#las inscripciones del archivo en un diccionario
	archivo.close()

loopPrincipal = True
time.sleep(5)																#Espera 5 segundos para que se vean los mensajes antes
while(loopPrincipal):														#de borrar la pantalla
	limpiar_pantalla()
	print("INGRESE EL NUMERO DE LA OPCION QUE DESEE UTILIZAR: ")
	print("--"*40)
	print("--"*40)
	print("1 : MENU PARA ENCARGADOS")
	print("--"*40)
	print("2 : MENU PARA PROFESORES")
	print("--"*40)
	print("0 : SALIR")
	print("--"*40)
	try:
		opcionPrincipal = int(input())										#Espera que el usuario ingrese una opcion valida
	except ValueError:														#Si no es una opcion valida muestra un mensaje de error
		limpiar_pantalla()
		print("Error al ingresar una opcion valida, intente de nuevo!")
		time.sleep(3)
		limpiar_pantalla()
	else:																	#Si la opcion es valida procede al menu de encargados o 
		limpiar_pantalla()													#al menu de profesores o sale del programa
		if(opcionPrincipal == 1):											
			loopEncargado = True
			while(loopEncargado):											#Validacion de encargados
				try:
					print("ENCARGADOS")										#Valida a un encargado primero revisando que su DNI sea valido
					print("--"*40)											#y luego revisando el DNI en las claves del diccionario
					print("Ingrese su DNI:")								#de encargados
					DNI = input()
					if(not validarDNI(DNI)):
						raise ValueError
					if(not validarEncargado(DNI)):
						raise Exception
					print("--"*40)
				except ValueError:											#Si el DNI es invalido lanza un error
					print("Error, dato invalido")
					print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu principal")
					opAux = input()
					if(opAux == '0'):
						loopEncargado = False
						print("Volviendo al menu principal")
					print("--"*40)
					time.sleep(3)
				except Exception:											#Si el DNI no esta en el diccionario lanza un error
					print("Error, no existe un encargado con los datos ingresados")
					print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu principal")
					opAux = input()
					if(opAux == '0'):
						loopEncargado = False
						print("Volviendo al menu principal")
					print("--"*40)
					time.sleep(3)
				else:														#De lo contrario el encargado es valido y procede al menu
					loopEncargado = False									#principal de encargados
					print("INGRESO EXITOSO")
					time.sleep(3)
					loopMenuEncargado = True
					while(loopMenuEncargado):										#Menu principal de encargados
						limpiar_pantalla()											
						print("A CONTINUACION INGRESE LA OPCION QUE DESEE UTILIZAR")		
						print("--"*40)														
						print("--"*40)
						print("1 : CREAR UNA INSCRIPCION")
						print("--"*40)
						print("2 : MODIFICAR UNA INSCRIPCION")
						print("--"*40)
						print("3 : ELIMINAR UNA INSCRIPCION")
						print("--"*40)
						print("0 : VOLVER AL MENU PRINCIPAL")
						print("--"*40)
						try:
							opcionEncargado = int(input())									#Espera que el encargado ingrese una opcion valida
						except ValueError:													#Si la opcion no es valida lanza un error
							limpiar_pantalla()												#Y vuelve a pedir por una opcion gracias al bucle while
							print("Error al ingresar una opcion valida, intente de nuevo!")
							time.sleep(3)
						else:																#De lo contrario se ejecuta la opcion que eligio el
							loopOpEncargado = True											#encargado
							if(opcionEncargado == 1):
								while(loopOpEncargado):										#Si la opcion fue 1, crea una inscripcion, pidiendo
									try:													#y validando los datos primero
										limpiar_pantalla()
										print("Ingrese la fecha de la nueva inscripcion con el formato DD/MM/YY:")
										fecha = input()
										if(not validarFecha(fecha)):										#Las fechas tienen que cumplir los
											raise ValueError												#parametro antes mencionados
										print("Ingrese el nombre del alumno de la nueva inscripcion:")
										alumno = input()
										if(not alumno.isalpha()):											#Los nombres de los alumnos y profesores
											raise ValueError												#deben ser solamente letras
										print("Ingrese el nombre de la materia de la nueva inscripcion:")
										materia = input()
										print("Ingrese el nombre del profesor de la nueva inscripcion:")
										profesor = input()
										if(not profesor.isalpha()):
											raise ValueError
										print("Ingrese el curso de la nueva inscripcion:")					#Los cursos y divisiones deben ser numeros
										curso = int(input())
										print("Ingrese la division de la nueva inscripcion")
										division = int(input())
										print("--"*40)
									except ValueError:														#Si algun dato no se cumple se lanza un error
										limpiar_pantalla()
										print("Error, dato invalido")
										print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu de encargados")
										opEncargado = input()
										if(opEncargado == '0'):
											loopOpEncargado = False
										print("--"*40)
									else:																										#Si los datos ingresados son validos
										limpiar_pantalla()																						#reviso primero si no hay una inscripcion
										if((fecha+alumno+materia) not in dicInscripciones.keys()):												#con los mismos datos en el diccionario
											Encargado.incorporarInscripcion(fecha, alumno, materia, profesor, curso, division, dicInscripciones)#de inscripciones. Si no hay, creo la
											print("Incorporacion de inscripcion exitosa! Volviendo al menu de encargados") 						#inscripcion, si muestro un mensaje de error
										else:
											print("Error, inscripcion ya almacenada")
											print("volviendo al menu de encargados en caso de que desee modificarla")
										loopOpEncargado = False
										print("--"*40)
										time.sleep(3)
							elif(opcionEncargado == 2):																		#Si la opcion fue 2 modifico una inscripcion
								while(loopOpEncargado):																		#primero pidiendo los datos de la inscripcion
									try:																					#que se desea modificar
										limpiar_pantalla()
										print("Ingrese la fecha de la inscripcion que desee modificar con el formato DD/MM/YY:")
										fecha = input()
										if(not validarFecha(fecha)):
											raise ValueError
										print("Ingrese el nombre del alumno en la inscripcion que desee modificar:")
										alumno = input()
										if(not alumno.isalpha()):
											raise ValueError
										print("Ingrese el nombre de la materia en la inscripcion que desee modificar:")
										materia = input()
										print("--"*40)
										if(fecha+alumno+materia not in dicInscripciones.keys()):
											raise Exception
									except ValueError:																		#Siguiendo los parametros mencionados se validan
										limpiar_pantalla()																	#los datos y se lanza un error si algun dato es invalido
										print("Error, dato invalido")
										print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu de encargados")
										opEncargado = input()
										if(opEncargado == '0'):
											loopOpEncargado = False
										print("--"*40)
									except Exception:																		#Se lanza un error si no hay un inscripcion con los datos
										limpiar_pantalla()																	#ingresados
										print("Error, la inscripcion ingresada no pertenece al sistema")
										print("Volviendo al menu de encargados")
										loopOpEncargado = False
										print("--"*40)
										time.sleep(3)
									else:																					#Si hay una inscripcion con los datos ingresados
										inscripcionAModificar = dicInscripciones[fecha+alumno+materia]						#ingreso al menu de modificacion de inscripciones
										while(loopOpEncargado):													
											limpiar_pantalla()
											print("--"*40)
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
											try:
												opEncargadoMod = int(input())												#Pido una opcion valida
												print("--"*40)
											except ValueError:																#Si no es valida lanzo un error y pido la opcion otra vez
												limpiar_pantalla()
												print("Error al ingresar una opcion valida, intente de nuevo!")
												print("--"*40)
												time.sleep(3)
											else:
												loopOpModificacion = True
												if(opEncargadoMod == 1):													#Dependiendo de la opcion se realizan diferentes cambios
													while(loopOpModificacion):												#Estos cambios son hechos sobre el diccionario creado al principio
														try:																# del programa. Una vez hecho un cambio se vuelve al menu de modificacion
															limpiar_pantalla()												#de inscripciones en caso de que se desee modificar algun otro dato
															print("Ingrese una nueva fecha para modificar la inscripcion ingresada anteriormente con el formato DD/MM/YY:")
															nuevaFecha = input()
															if(not validarFecha(nuevaFecha)):
																raise ValueError
															print("--"*40)
														except ValueError:
															limpiar_pantalla()
															print("Error, fecha no valida, intente de nuevo!")
															print("--"*40)
															time.sleep(3)
														else:
															limpiar_pantalla()
															Encargado.modificarFecha(inscripcionAModificar, nuevaFecha)
															print("Fecha en la inscripcion modificada con exito!")
															loopOpModificacion = False
															print("--"*40)
															time.sleep(3)
												elif(opEncargadoMod == 2):
													while(loopOpModificacion):
														try:
															limpiar_pantalla()
															print("Ingrese el nuevo nombre del alumno para modificar la inscripcion ingresada anteriormente:")
															nuevoAlumno = input()
															if(not nuevoAlumno.isalpha()):
																raise ValueError
															print("--"*40)
														except ValueError:
															limpiar_pantalla()
															print("Error, alumno no valido, intente de nuevo!")
															print("--"*40)
															time.sleep(3)
														else:
															limpiar_pantalla()
															Encargado.modificarAlumno(inscripcionAModificar, nuevoAlumno)
															print("Nombre del alumno en la inscripcion modificado con exito!")
															loopOpModificacion = False
															print("--"*40)
															time.sleep(3)
												elif(opEncargadoMod == 3):
													limpiar_pantalla()
													print("Ingrese la nueva materia para modificar la inscripcion ingresada anteriormente:")
													nuevaMateria = input()
													Encargado.modificarMateria(inscripcionAModificar, nuevaMateria)
													print("--"*40)
													limpiar_pantalla()
													print("Materia en la inscripcion modificada con exito!")
													print("--"*40)
													time.sleep(3)
												elif(opEncargadoMod == 4):
													while(loopOpModificacion):
														try:
															limpiar_pantalla()
															print("Ingrese el nuevo nombre del profesor para modificar la inscripcion ingresada anteriormente:")
															nuevoProfesor = input()
															if(not nuevoProfesor.isalpha()):
																raise ValueError
															print("--"*40)
														except ValueError:
															limpiar_pantalla()
															print("Error, profesor no valido, intente de nuevo")
															print("--"*40)
															time.sleep(3)
														else:
															limpiar_pantalla()
															Encargado.modificarProfesor(inscripcionAModificar, nuevoProfesor)
															print("Nombre del profesor en la inscripcion modificado con exito!")
															loopOpModificacion = False
															print("--"*40)
															time.sleep(3)
												elif(opEncargadoMod == 5):
													while(loopOpModificacion):
														try:
															limpiar_pantalla()
															print("Ingrese el nuevo numero de curso para modificar la inscripcion ingresada anteriormente:")
															nuevoCurso = int(input())
															print("--"*40)
														except ValueError:
															limpiar_pantalla()
															print("Error, curso no valido, intente de nuevo")
															print("--"*40)
															time.sleep(3)
														else:
															limpiar_pantalla()
															Encargado.modificarCurso(inscripcionAModificar, nuevoCurso)
															print("Curso en la inscripcion modificado con exito!")
															loopOpModificacion = False
															print("--"*40)
															time.sleep(3)
												elif(opEncargadoMod == 6):
													while(loopOpModificacion):
														try:
															limpiar_pantalla()
															print("Ingrese el nuevo numero de division para modificar la inscripcion ingresada anteriormente:")
															nuevaDivision = int(input())
															print("--"*40)
														except ValueError:
															limpiar_pantalla()
															print("Error, division no valida, intente de nuevo")
															print("--"*40)
															time.sleep(3)
														else:
															limpiar_pantalla()
															Encargado.modificarDivision(inscripcionAModificar, nuevaDivision)
															print("Division en la inscripcion modificada con exito!")
															loopOpModificacion = False
															print("--"*40)
															time.sleep(3)
												elif(opEncargadoMod == 0):									#Si la opcion en el menu de modificaciones del encargado
													limpiar_pantalla()										#fue 0 vuelvo al menu de encargados poniendo en falso
													print("Volviendo al menu de encargados!")				#la bandera booleana del bucle para el menu de modificaciones
													loopOpEncargado = False
													print("--"*40)
													time.sleep(3)
												else:
													limpiar_pantalla()
													print("Error al ingresar una opcion valida, intente de nuevo!")
													print("--"*40)
													time.sleep(3)
							elif(opcionEncargado == 3):																#Si la opcion en el menu de encargados fue 3
								while(loopOpEncargado):																#pido los datos de una inscripcion
									try:																			#y los valido
										limpiar_pantalla()
										print("Ingrese la fecha de la inscripcion que desee eliminar con el formato DD/MM/YY:")
										fecha = input()
										if(not validarFecha(fecha)):
											raise ValueError
										print("Ingrese el nombre del alumno en la inscripcion que desee eliminar:")
										alumno = input()
										if(not alumno.isalpha()):
											raise ValueError
										print("Ingrese el nombre de la materia en la inscripcion que desee eliminar:")
										materia = input()
										print("--"*40)
									except ValueError:
										limpiar_pantalla()
										print("Error, dato invalido")
										print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu de encargados")
										opEncargado = input()
										if(opEncargado == '0'):
											loopOpEncargado = False
										print("--"*40)
									else:
										limpiar_pantalla()
										if(fecha+alumno+materia in dicInscripciones.keys()):											#Si hay una inscripcion con los datos
											Encargado.eliminarInscripcion(dicInscripciones[fecha+alumno+materia], dicInscripciones) 	#ingresados la elimino
											print("La inscripcion ingresada fue eliminada con exito! volviendo al menu de encargados")
										else:																							#Si no la hay muestro un mensaje de error
											print("Error, la inscripcion ingresada no pertenece al sistema")
											print("Volviendo al menu de encargados")
										loopOpEncargado = False
										print("--"*40)
										time.sleep(3)
							elif(opcionEncargado == 0):													#Si la opcion en el menu de encargados fue 0
								limpiar_pantalla()														#vuelvo al menu principal poniendo en falso el bucle
								print("Volviendo al menu principal!")									#del menu encargado y actualizo las inscripciones
								loopMenuEncargado = False												#en el archivo de texto para que se
								actualizarInscripciones()												#puedan visualizar los cambios
								print("--"*40)
								time.sleep(3)
							else:
								limpiar_pantalla()														#Si la opcion en el menu de encargados fue un numero
								print("Error al ingresar una opcion valida, intente de nuevo!")			#no indicado en la opciones, muestro un error y vuelvo
								time.sleep(3)															#al menu principal
		elif(opcionPrincipal == 2):
			loopProfesor = True
			while(loopProfesor):																#Si la opcion en el menu principal fue un 2 ingreso
				try:																			#a la validacion de profesores
					limpiar_pantalla()															#Un profesor se valida con una clave de tipo string
					print("PROFESORES")															#formada por su nombre concatenada con la materia que dicta
					print("--"*40)
					print("Ingrese su nombre:")
					nombre = input()
					print("Ingrese la materia que dicta:")
					materia = input()
					if((nombre+materia) not in dicProfesores.keys()):							#Si el profesor no esta en el diccionario de profesores
						raise Exception															#cargado al principio del programa lanzo un error
					print("--"*40)	
				except ValueError:
					limpiar_pantalla()
					print("Error, dato invalido")
					print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu principal")
					opAux = input()
					if(opAux == '0'):
						loopProfesor = False
						print("Volviendo al menu principal")
					print("--"*40)
					time.sleep(3)
				except Exception:
					limpiar_pantalla()
					print("Error, no existe un profesor con los datos ingresados")
					print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu principal")
					opAux = input()
					if(opAux == '0'):
						loopProfesor = False
						print("Volviendo al menu principal")
					print("--"*40)
					time.sleep(3)
				else:																			#De lo contrario el profesor ingresado es valido
					limpiar_pantalla()															#y puede proceder al menu de profesores
					loopProfesor = False
					print("--"*40)
					print("INGRESO EXITOSO")
					print("--"*40)
					time.sleep(3)
					loopMenuProfesor = True
					while(loopMenuProfesor):															#Muestro las opciones del menu de profesores
						limpiar_pantalla()
						print("A CONTINUACION INGRESE LA OPCION QUE DESEE UTILIZAR")
						print("--"*40)
						print("--"*40)
						print("1 : MODIFICAR UNA NOTA")
						print("--"*40)
						print("2 : ELIMINAR UNA NOTA")
						print("--"*40)
						print("0 : VOLVER AL MENU PRINCIPAL")
						print("--"*40)
						try:
							opMenuProfesor = int(input())												#Espero por una opcion valida
							print("--"*40)
						except ValueError:
							limpiar_pantalla()
							print("Error al ingresar una opcion valida, intente de nuevo!")
							print("--"*40)
							time.sleep(3)
						else:
							loopOpProfesor = True
							if(opMenuProfesor == 1):													#Si la opcion es 1, procedo a validar los datos
								while(loopOpProfesor):													#de la inscripcion que se desee modificar su nota
									try:
										limpiar_pantalla()
										print("Ingrese la fecha de la inscripcion que desee modificar con el formato DD/MM/YY:")
										fecha = input()
										if(not validarFecha(fecha)):
											raise ValueError
										print("Ingrese el nombre del alumno en la inscripcion que desee modificar:")
										alumno = input()
										if(not alumno.isalpha()):
											raise ValueError
										print("Ingrese el nombre de la materia en la inscripcion que desee modificar:")
										materiaInscripcion = input()
										if(not materiaInscripcion == materia):							#Si el profesor ingresado no dicta la misma materia
											raise Exception												#que la materia de la inscripcion ingresada lanzo
										print("--"*40)													#un error
									except ValueError:
										limpiar_pantalla()
										print("Error, dato invalido")
										print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu de profesores")
										opProfesor = input()
										if(opProfesor == '0'):
											loopOpProfesor = False
										print("--"*40)
									except Exception:
										limpiar_pantalla()
										print("Error, materia invalida")
										print("No puede cambiar la nota de un examen de una materia de la que no es profesor, intente de nuevo")
										print("--"*40)
										time.sleep(3)
									else:
										loopOpProfesor = False													#Si los datos fueron validados correctamente
										if(fecha+alumno+materiaInscripcion in dicInscripciones.keys()):			#y existe una inscripcion con esos datos
											loopOpModificacion = True											#le pido la nueva nota al profesor
											while(loopOpModificacion):
												limpiar_pantalla()
												try:
													print("Ingrese la nueva nota de la inscripcion ingresada anteriormente:")
													nuevaNota = int(input())
													if(0 <= nuevaNota > 10):									#La nota debe ser mayor que 0 y menor o igual a 10
														raise Exception
												except ValueError:
													limpiar_pantalla()
													print("Error, nota no valida, vuelva a intentarlo")
													print("--"*40)
													time.sleep(3)
												except Exception:
													limpiar_pantalla()
													print("Error, la nota debe ser un numero del 1 al 10, vuelva a intentarlo")
													print("--"*40)
													time.sleep(3)
												else:
													limpiar_pantalla()											#Si la nota es valida, modifico la nota de la inscripcion en el diccionario
													Profesor.modificarNota(dicInscripciones[fecha+alumno+materia], nuevaNota)
													print("Nota en la inscripcion ingresada modificada con exito!")
													loopOpModificacion = False
										else:
											limpiar_pantalla()
											print("Error, la inscripcion ingresada no pertenece al sistema")
											print("Volviendo al menu de profesores")
										print("--"*40)
										time.sleep(3)
							elif(opMenuProfesor == 2):													#Si la opcion es 2, procedo a validar los datos
								while(loopOpProfesor):													#de la inscripcion que se desee eliminar su nota
									try:																#Eliminar una nota consiste en poner el campo de la
										limpiar_pantalla()												#inscripcion en -1
										print("Ingrese la fecha de la inscripcion que desee eliminar su nota con el formato DD/MM/YY:")
										fecha = input()
										if(not validarFecha(fecha)):
											raise ValueError
										print("Ingrese el nombre del alumno en la inscripcion que desee eliminar su nota:")
										alumno = input()
										if(not alumno.isalpha()):
											raise ValueError
										print("Ingrese el nombre de la materia en la inscripcion que desee eliminar su nota:")
										materia = input()
										print("--"*40)
									except ValueError:
										limpiar_pantalla()
										print("Error, dato invalido")
										print("Intente otra vez ingresando cualquier tecla, o '0' para volver al menu de profesores")
										print("--"*40)
										opProfesor = input()
										if(opProfesor == '0'):
											loopOpProfesor = False
									else:
										limpiar_pantalla()
										loopOpProfesor = False
										if(fecha+alumno+materia in dicInscripciones.keys()):					#Si la inscripcion ingresada esta en el diccionario
											Profesor.eliminarNota(dicInscripciones[fecha+alumno+materia])		#de inscripciones, procedo a eliminar la nota
											print("La nota de la inscripcion ingresada fue eliminada con exito! Volviendo al menu de profesores")
										else:
											print("Error, la inscripcion ingresada no pertenece al sistema")
											print("Volviendo al menu de profesores")
										print("--"*40)
										time.sleep(3)
							elif(opMenuProfesor == 0):															#Si la opcion es 0 en el menu de profesores vuelvo
								limpiar_pantalla()																#al menu principal y tambien
								print("Volviendo al menu principal!")											#actualizo las inscripciones en 
								loopMenuProfesor = False														#el archivo de texto para que se 
								print("--"*40)																	#puedan visualizar los cambios
								actualizarInscripciones()
								time.sleep(3)
							else:																				#Si la opcion es un numero 
								limpiar_pantalla()																#no indicado en la opciones,
								print("Error al ingresar una opcion valida, intente de nuevo!")					#muestro un error y vuelvo
								print("--"*40)																	#al menu principal
								time.sleep(3)
		elif(opcionPrincipal == 0):													#Si la opcion en el menu principal
			limpiar_pantalla()														#es 0 muestro un mensaje y actualizo las inscripciones
			print("GRACIAS POR UTILIZAR EL SISTEMA DE INSCRIPCIONES!")				#del diccionario de inscripciones en
			print("--"*40)															#el archivo de texto 'Inscripciones'
			actualizarInscripciones()
			loopPrincipal = False
			time.sleep(3)
		else:
			limpiar_pantalla()
			print("Error al ingresar una opcion valida, intente de nuevo!")
			print("--"*40)
			time.sleep(3)