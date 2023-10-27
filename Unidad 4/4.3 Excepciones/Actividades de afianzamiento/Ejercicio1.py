#Ejercicio 1
#Construya un programa que permita que transforme un string
#a un número. Controle las situaciones de error usando excepciones.


loop = True
while(loop):
	try:
		print("Ingrese un string para saber si se puede transformar a entero:")
		num = int(input())
	except ValueError:
		print("El string ingresado no puede ser transformado a entero, vuelva a intentarlo!")
	else:
		print("El string fue transformado a entero de manera satisfactoria!")
		loop = False