#Ejercicio 9
#Escriba un programa que sume los números que se encuentran
#en un archivo de texto cuyo nombre es ingresado por el usuario.


numeros = {"0","1","2","3","4","5","6","7","8","9"}

loop = True
while(loop):
	try:
		print("Ingrese el nombre del archivo que desee calcular la suma de los numeros en el archivo: ")
		ruta = str(input())

		archivo = open(ruta, "r")
		texto = archivo.readlines()
		archivo.close()

		suma = 0
		for linea in texto:
			linea = linea.rstrip('''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''')
			for palabra in linea.split(" "):
				for simbolo in palabra:
					if(simbolo in numeros):
						suma = suma + int(simbolo)

		print("La suma de todos los numeros del texto ingresado da como resultado", suma)
		loop = False

	except ValueError:
		print("Se ingreso un dato invalido, vuelva a intentarlo!")
	except FileNotFoundError:
		print("El nombre del archivo ingresado no pertenece a ningun archivo, vuelva a intentarlo!")