#Ejercicio 2
#Escriba un programa que permita insertar, modificar y eliminar
#elementos de una lista. Controle la situaciones de error usando
#excepciones.


lista = []
loop = True
while(loop):
	try:
		print("--"*40)
		print("Ingrese el numero de la opcion deseada para editar la lista:")
		print("--"*40)
		print("1 : INSERTAR EN LA LISTA")
		print("--"*40)
		print("2 : MODIFICAR UN ELEMENTO DE LA LISTA")
		print("--"*40)
		print("3 : ELIMINAR UN ELEMENTO DE LA LISTA")
		print("--"*40)
		print("4 : MOSTRAR LOS ELEMENTOS DE LA LISTA")
		print("--"*40)
		print("0 : SALIR")
		print("--"*40)

		opcion = int(input())
	except ValueError:
		print("Ingreso una opcion no valida, vuelva a intentarlo!")
	else:
		repetirOpcion = True
		if(opcion == 1):
			while(repetirOpcion):
				try:
					print("Ingrese el elemento que desee insertar:")
					ele = input()
					print("Inserte la posicion en la lista que desea insertar el elemento")
					pos = int(input())
					lista.insert(pos, ele)
				except ValueError:
					print("Ingreso una posicion no valida, vuelva a intentarlo!")
				except IndexError:
					print(f"Posicion no valida, asegurese de ingresar una posicion del 0 al {len(lista)-1}!")
				else:
					print("El elemento ingresado fue insertado en la posicion dada!")
					repetirOpcion = False
		elif(opcion == 2):
			while(repetirOpcion):
				try:
					print("Ingrese la posicion del elemento que desee modificar:")
					pos = int(input())
					print("Inserte el elemento nuevo para reemplazar:")
					ele = input()
					lista[pos] = ele
				except ValueError:
					print("Ingreso una posicion no valida, vuelva a intentarlo!")
				except IndexError:
					print(f"Posicion no valida, asegurese de ingresar una posicion del 0 al {len(lista)-1}!")
				else:
					print("El elemento en la posicion ingresada fue reemplazado por el elemento ingresado!")
					repetirOpcion = False
		elif(opcion == 3):
			while(repetirOpcion):
				try:
					print("Ingrese la posicion del elemento que desee eliminar:")
					pos = int(input())
					ele = lista.pop(pos)
				except ValueError:
					print("Ingreso una posicion no valida, vuelva a intentarlo!")
				except IndexError:
					print(f"Posicion no valida, asegurese de ingresar una posicion del 0 al {len(lista)-1}!")
				else:
					print("El elemento en la posicion ingresada,", ele, ", fue eliminado de la lista!")
					repetirOpcion = False
		elif(opcion == 4):
			print("La lista es la siguiente, recuerde que solo puede editar la lista con posiciones comenzando del cero!")
			print(lista)
		elif(opcion == 0):
			print("Gracias por utilizar el editor de lista!")
			loop = False
		else:
			print("Ingreso una opcion no valida, vuelva a intentarlo!")