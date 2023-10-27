#Ejercicio 7
#Escriba un programa que pase a mayúsculas todas las letras que
#contiene un archivo a minúsculas. El nombre del archivo es ingresado
#por el usuario.


loop = True
while(loop):
	try:
		print("Ingrese el nombre del archivo que desee pasar su contenido a mayusculas: ")
		ruta = str(input())

		archivo = open(ruta, "r")
		texto = archivo.readlines()
		archivo.close()

		archivo = open(ruta, "w")
		for linea in texto:
			archivo.write(linea.upper())

		archivo.close()
		print("El archivo fue pasado a mayusculas con exito!")
		loop = False
	except ValueError:
		print("Se ingreso un dato invalido, vuelva a intentarlo!")
	except FileNotFoundError:
		print("El nombre del archivo ingresado no pertenece a ningun archivo, vuelva a intentarlo!")
