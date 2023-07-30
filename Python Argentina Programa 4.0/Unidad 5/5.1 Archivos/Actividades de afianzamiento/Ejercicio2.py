#Ejercicio 2
#Escriba un programa que permita que el usuario ingrese el
#nombre de un archivo lo abra y escriba una cadena de carácteres ingresada
#por el usuario. Luego el programa debe cerrar el archivo.


loop = True
while(loop):
	try:
		print("Ingrese la ruta del archivo que desee escribir: ")
		archivo = open(str(input()), "a")

		print("Ingrese la cadena de caracteres que desee agregar al archivo: ")
		cadena = str(input())

		archivo.write(cadena)

		archivo.close()

		loop = False
	except ValueError:
		print("Se ingreso un simbolo no valido, vuelva a intentarlo!")
	except FileNotFoundError:
		print("La ruta del archivo ingresada no pertenece a ningun archivo de texto, vuelva a intentarlo!")