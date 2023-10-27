#Ejercicio 12
#Escriba un programa que invierta el orden y a su vez las
#palabras de un archivo de texto.


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
			linea.rstrip()
			for palabra in linea.split():
				archivo.write(palabra[::-1])
				archivo.write(" ")
			archivo.write("\n")

		archivo.close()
		print("Las palabras del archivo de texto y el orden de sus lineas fueron invertidas de manera satisfactoria!")
		loop = False
	except ValueError:
		print("Se ingreso un dato invalido, vuelva a intentarlo!")
	except FileNotFoundError:
		print("El nombre del archivo ingresado no pertenece a ningun archivo, vuelva a intentarlo!")