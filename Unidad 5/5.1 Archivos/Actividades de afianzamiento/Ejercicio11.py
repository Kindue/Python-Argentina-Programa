#Ejercicio 11
#Escriba un programa que invierta las palabras de un archivo
#de texto.


def invertirPalabra(palabra):
	return palabra[::-1]

loop = True
while(loop):
	try:
		print("Ingrese el nombre del archivo que desee invertir sus palabras: ")
		ruta = str(input())

		archivo = open(ruta, "r")
		texto = archivo.readlines()
		archivo.close()

		archivo = open(ruta, "w")
		for linea in texto:
			linea = linea.rstrip()
			for palabra in linea.split():
				archivo.write(palabra[::-1])
				archivo.write(" ")
			archivo.write("\n")

		archivo.close()
		print("Las palabras del archivo de texto fueron invertidas de manera satisfactoria!")
		loop = False
	except ValueError:
		print("Se ingreso un dato invalido, vuelva a intentarlo!")
	except FileNotFoundError:
		print("El nombre del archivo ingresado no pertenece a ningun archivo, vuelva a intentarlo!")