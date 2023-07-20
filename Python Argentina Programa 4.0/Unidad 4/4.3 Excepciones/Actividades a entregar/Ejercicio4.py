#Ejercicio 4
#Escriba un programa que permita que el usuario cree un diccio-
#nario. El programa permite: insertar, eliminar y modificar los elementos
#del diccionario. Cuando se desea insertar un valor cuya clave ya existe
#el programa dispara una excepción KeyError cuyo manejador pregun-
#ta al usuario si realmente desea modificar el valor. En caso afirmativo
#realiza la modificación correspondiente. En caso negativo el programa
#no realiza ninguna acción. El programa también debe manejar los erro-
#res por intento de acceso incorrecto al diccionario y otros que puedan
#surgir utilizando una clave incorrecta.



d = {}
loop = True

while(loop):
	print("Ingrese el numero de la opcion para editar el diccionario creado")
	print("1 : Insertar entrada   2 : Eliminar entrada   3 : Modificar entrada")
	print("--"*40)
	op1 = int(input())


	if(op1 == 1):
		try:
			print("Ingrese la clave de la entrada que desea ingresar al diccionario: ")
			clave = input()
			if(clave in d.keys()):
				raise KeyError()
			else:
				print("Ingrese el valor correspondiente a la clave recien ingresada: ")
				valor = input()
				d[clave] = valor
				print("Se inserto con exito la clave!")
		except:
			k = input("KeyError! Esta clave ya existe en el diccionario desea reemplazarla por el valor ingresado? (S/N) ")
			if(k.upper() == "S"):
				print("Ingrese el valor correspondiente a la clave recien ingresada: ")
				valor = input()
				d[clave] = valor
				print("La clave fue modificada con exito!")
			elif(k.upper() == "N"):
				print("La clave no fue modificada!")
			else:
				print("Opcion no valida, vuelva a intentarlo desde el inicio!")
	elif(op1 == 2):
		try:
			print("Ingrese la clave que desee eliminar del diccionario: ")
			clave = input()
			d.pop(clave)
			print("La entrada fue eliminada con exito!")
		except:
			print("KeyError! La clave ingresada no existe en el diccionario, no se pudo remover!")
	elif(op1 == 3):
		try:
			print("Ingrese la clave de la entrada que desee modificar: ")
			clave = input()
			if(clave not in d.keys()):
				raise KeyError()
			else:
				print("Ingrese el nuevo valor de la entrada que desee modificar: ")
				valor = input()
				d[clave] = valor
				print("La clave fue modificada con exito!")
		except:
			print("KeyError! La clave ingresada no esta en el diccionario, no se pudo modificar!")
	else:
		print("Opcion no valida vuelva a intentarlo!")

	print("--"*40)
	print("Ingrese 0 para terminar o cualquier otra tecla para continuar editando el diccionario! ")
	op2 = input()
	print("--"*40)
	if(op2 == '0'):
		loop = False
