#Ejercicio 3
#Escriba un programa que permita que el usuario agregue la
#cadena "Fin de Archivo" al final de un archivo cuyo nombre es ingresado
#por teclado.


loop = True
while(loop):
	try:
		print("Ingrese la ruta del archivo que desee editar: ")
		ruta = str(input())
		archivo = open(ruta, "r")
		archivo.close()
		archivo = open(ruta, "a")

		archivo.write("\n")
		archivo.write("Fin de Archivo!")
		archivo.close()

		loop = False
	except ValueError:
		print("Se ingreso un simbolo incorrecto, vuelva a intentarlo!")
	except FileNotFoundError:
		print("La ruta del archivo ingresada no coincide con ningun archivo existente, vuelva a intentarlo!")