#Ejercicio 6
#Escriba un programa que permita que el usuario ingrese el nombre
#de un archivo. Luego el programa debe leer el archivo y contabilizar
#para cada palabra que aparece en el archivo la cantidad de veces que
#la misma se repite. Luego el programa debe imprimir por pantalla las
#cinco palabras que más se repitieron en el archivo.


loop = True
while(loop):
	try:
		print("Ingrese el nombre del archivo que desee leer y contabilizar sus palabras: ")
		ruta = str(input())

		archivo = open(ruta, "r")
		texto = archivo.readlines()
		dicAux = {}
		for linea in texto:
			linea = linea.rstrip('''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''')
			for palabra in linea.split(" "):
				if(palabra.upper() not in dicAux):
					dicAux[palabra.upper()] = 0
				else:
					dicAux[palabra.upper()] += 1

		for i in range(5):
			if(len(dicAux) > 0):
				cant = 0
				mayor = ""
				for pal in dicAux.keys():
					if(dicAux[pal] >= cant):
						mayor = pal
						cant = dicAux[pal]
				dicAux.pop(mayor)
				print(f"La palabra '{mayor}' se repite {cant} veces.")

		loop = False
	except ValueError:
		print("Se ingreso un dato invalido, vuelva a intentarlo!")
	except FileNotFoundError:
		print("El nombre del archivo ingresado no pertenece a ningun archivo, vuelva a intentarlo!")