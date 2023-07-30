#Ejercicio 10
#Escriba un programa que invierta el orden de las líneas de un
#archivo de texto.


loop = True
while(loop):
	try:
		print("Ingrese el nombre del archivo que desee invertir el orden de sus lineas: ")
		ruta = str(input())

		archivo = open(ruta, "r")
		texto = archivo.readlines()
		archivo.close()

		lista = []
		for linea in texto:
			lista.append(linea.rstrip())

		lista.reverse()
		archivo = open(ruta, "w")
		for linea in lista:
			archivo.write(linea)
			archivo.write("\n")

		archivo.close()

		print("El orden de las lineas del archivo ingresado ha sido invertido con exito!")
		loop = False
	except ValueError:
		print("Se ingreso un dato invalido, vuelva a intentarlo!")
	except FileNotFoundError:
		print("El nombre del archivo ingresado no pertenece a ningun archivo, vuelva a intentarlo!")