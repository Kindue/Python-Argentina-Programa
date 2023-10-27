#Ejercicio 5 
#Escriba un programa que permita que el usuario cree un archivo
#y le grabe n cadena de caracteres.


loop = True
while(loop):
	try:
		print("Ingrese el nombre del archivo que desee crear con la extension .txt al final: ")
		ruta = str(input())

		print("Ingrese la cantidad de veces que desee escribir la cadena de caracteres: ")
		cant = int(input())

		print("Ingrese la cadena de caracteres que desee escribir en el nuevo archivo: ")
		cadena = str(input())

		archivo = open(ruta, "w")
		for i in range(cant):
			archivo.write(cadena + " ")

		archivo.close()
		loop = False
		print("El archivo con", cant, "'" + cadena + "' fue creado!")
	except ValueError:
		print("Se ingreso un dato de manera incorrecta, vuelva a intentarlo!")