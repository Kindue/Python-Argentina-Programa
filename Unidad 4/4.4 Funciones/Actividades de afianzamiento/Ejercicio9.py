#Ejercicio 9
#Implemente un padrón de personas. Por cada persona se
#almacena el nombre, dni y domicilio. El programa debe permitir que el
#usuario pueda:
#1. Incorporar personas al padrón.
#2. Eliminar personas del padrón.
#3. Modificar los datos de una persona en el padrón.
#4. Imprimir por pantalla los datos de una persona específica.
#El programa debe mostrar por pantalla un menú de opciones con los
#ítems descritos anteriormente. El programa finalizará si el usuario
#ingresa como opción un 0.



padron = {}

def incorporarPersona(dni, nombre, domicilio):
	padron[dni] = {"nombre": nombre, "domicilio": domicilio}

def eliminarPersona(dni):
	padron.pop(dni)

def setDNI(dni, nuevoDNI):
	nombreAux = padron[dni]["nombre"]
	domicilioAux = padron[dni]["domicilio"]
	padron.pop(dni)
	padron[nuevoDNI] = {"nombre" : nombreAux, "domicilio" : domicilioAux} 

def setNombre(dni, nuevoNombre):
	padron[dni]["nombre"] = nuevoNombre

def setDomicilio(dni, nuevoDomicilio):
	padron[dni]["domicilio"] = nuevoDomicilio

def toString(dni):
	return (f"DNI: {dni} Nombre: { padron[dni]['nombre'] } Domicilio: { padron[dni]['domicilio'] } ")

def validarDNI(dni):
	dni = str(dni)
	if(len(dni) >= 7) and (len(dni) <= 8):
		return True
	else:
		return False


#PROGRAMA PRINCIPAL

loop = True
print("Bienvenido al padron de personas")
while(loop):
	print("--"*40)
	print("Ingrese el numero de la opcion deseada")
	print("--"*40)
	print("1 : Incorporar una persona al padron")
	print("--"*40)
	print("2 : Eliminar una persona del padron")
	print("--"*40)
	print("3 : Modificar una persona del padron")
	print("--"*40)
	print("4 : Mostrar la informacion de una persona del padron")
	print("--"*40)
	print("0 : Salir del padron de personas")
	print("--"*40)
	print()
	try:
		opcion = int(input())
	except ValueError:
		print("Ingreso una opcion invalida, por favor intentelo de nuevo!")
	else:
		if(opcion == 1):
			repetirOpcion = True
			while(repetirOpcion):
				try:
					print("--"*40)
					print("Ingrese los datos de la persona que desee incorporar al padron: ")
					print("Ingrese el DNI de la persona")
					print("O ingrese 0 para volver al menu principal")
					dni = int(input())
					if(dni != 0):
						if(validarDNI(dni)):
							if(dni not in padron):
								print("Ingrese el nombre de la persona:")
								nombre = str(input())
								print("Ingrese el domicilio de la persona:")
								domicilio = str(input())
								incorporarPersona(dni, nombre, domicilio)
								repetirOpcion = False
								print("Se ingreso la persona al padron de manera exitosa!")
							else:
								print("El DNI ingresado ya pertenece al padron, si desea modificarlo vuelva al menu principal!")
						else:
							print("El DNI ingresado no es valido, por favor intentelo de nuevo!")
					else:
						repetirOpcion = False
						print("Volviendo al menu principal!")
				except ValueError:
					print("Error, se ingreso un dato no correcto, por favor intentelo de nuevo!")
		elif(opcion == 2):
			repetirOpcion = True
			while(repetirOpcion):
				try:
					print("--"*40)
					print("Ingrese el DNI de la persona que quiere remover del padron")
					print("O ingrese 0 para volver al menu principal")
					dni = int(input())
					if(dni != 0):
						if(validarDNI(dni)):
							if(dni in padron.keys()):
								eliminarPersona(dni)
								repetirOpcion = False
								print("La persona fue eliminada del padron de manera exitosa!")
							else:
								print("El DNI que se ingreso no pertenece al padron, intentelo de nuevo!")
						else:
							print("El DNI no es valido, por favor intentelo de nuevo!")
					else:
						repetirOpcion = False
						print("Volviendo al menu principal!")
				except ValueError:
					print("Error, el DNI ingresado no esta conformado por numeros, por favor intentelo de nuevo!")
		elif(opcion == 3):
			repetirOpcion = True
			while(repetirOpcion):
				try:
					print("--"*40)
					print("Ingrese el DNI de la persona que desee modificar")
					print("O ingrese 0 para volver al menu principal")
					dni = int(input())
					if(dni != 0):
						if(validarDNI(dni)):
							if(dni in padron.keys()):
								print("--"*40)
								print("Ingrese el numero de la opcion deseada:")
								print("--"*40)
								print("1 : Modificar su DNI en el padron")
								print("--"*40)
								print("2 : Modificar su nombre en el padron")
								print("--"*40)
								print("3 : Modificar su domicilio en el padron")
								print("--"*40)
								print("0 : Volver al menu principal")
								print("--"*40)
								op = int(input())
								if(op == 1):
									print("Ingrese el nuevo DNI de la persona:")
									nuevoDNI = int(input())
									if(validarDNI(nuevoDNI)):
										setDNI(dni, nuevoDNI)
										print("DNI modificado con exito!")
									else:
										print("El nuevo DNI ingresado no es valido, vuelva a intentarlo!")
								elif(op == 2):
									print("Ingrese el nuevo nombre de la persona:")
									nuevoNombre = str(input())
									setNombre(dni, nuevoNombre)
									print("Nombre modificado con exito!")
								elif(op == 3):
									print("Ingrese el nuevo domicilio de la persona:")
									nuevoDomicilio = str(input())
									setDomicilio(dni, nuevoDomicilio)
									print("Domicilio modificado con exito!")
								elif(op == 0):
									repetirOpcion = False
									print("Volviendo al menu principal!")
								else:
									print("Error al ingresar una opcion valida, vuelva a intentarlo!")
							else:
								print("El DNI ingresado no esta en el padron, vuelva a intentarlo!")
						else:
							print("El DNI ingresado no es valido, vuelva a intentarlo!")
					else:
						repetirOpcion = False
						print("Volviendo al menu principal!")
				except ValueError:
					print("Error al ingresar una opcion valida o un DNI valido, vuelva a intentarlo!")
		elif(opcion == 4):
			repetirOpcion = True
			while(repetirOpcion):
				try:	
					print("--"*40)
					print("Ingrese el DNI de la persona que desee visualizar su informacion en el padron")
					print("O ingrese 0 para volver al menu principal")
					dni = int(input())
					if(dni != 0):
						if(validarDNI(dni)):
							if(dni in padron.keys()):
								print("Los datos de la persona con el DNI ingresado son los siguientes:")
								print(toString(dni))
								repetirOpcion = False
							else:
								print("El dni ingresado no esta en el padron!")
						else:
							print("El DNI ingresado no es valido, vuelva a intentarlo")
					else:
						repetirOpcion = False
						print("Volviendo al menu principal!")
				except ValueError:
					print("Error al ingresar un DNI valido, vuelva a intentarlo!")
		elif(opcion == 0):
			print("--"*40)
			print("Gracias por utilizar el padron de personas!")
			loop = False
		else:
			print("Error al ingresar una opcion valida, intentelo de nuevo!")