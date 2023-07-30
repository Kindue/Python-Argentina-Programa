#Ejercicio 8
#Escriba un programa que cuente la cantidad de: mayúsculas,
#minúsculas y números que contiene un archivo ingresado por el usuario.


minusculas = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","á","é","í","ó","ú","ñ"}
mayusculas = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Á","É","Í","Ó","Ú","Ñ"}
numeros = {"0","1","2","3","4","5","6","7","8","9"}

loop = True
while(loop):
	try:
		print("Ingrese el nombre del archivo que desee contar cuantas mayusculas, minusculas y numeros el archivo posee: ")
		ruta = str(input())

		archivo = open(ruta, "r")
		texto = archivo.readlines()
		archivo.close()

		contMinusculas = 0
		contMayusculas = 0
		contNumeros = 0
		for linea in texto:
			linea = linea.rstrip('''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''')
			for palabra in linea.split(" "):
				for simbolo in palabra:
					if(simbolo in minusculas):
						contMinusculas += 1
					elif(simbolo in mayusculas):
						contMayusculas += 1
					elif(simbolo in numeros):
						contNumeros += 1

		print("El archivo tiene", contMinusculas, "minusculas")
		print("El archivo tiene", contMayusculas, "mayusculas")
		print("El archivo tiene", contNumeros, "numeros")

		loop = False
	except ValueError:
		print("Se ingreso un dato invalido, vuelva a intentarlo!")
	except FileNotFoundError:
		print("El nombre del archivo ingresado no pertenece a ningun archivo, vuelva a intentarlo!")