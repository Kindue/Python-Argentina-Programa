#Ejercicio 4
#Escriba un programa que permita que el usuario cree un diccio-
#nario. El programa permite: insertar, eliminar y modificar los elementos
#del diccionario. Cuando se desea insertar un valor cuya clave ya existe
#el programa dispara una excepción KeyError cuyo manejador pregun-
#ta al usuario si realmente desea modificar el valor. En caso afirmativo
#realiza la modificación correspondiente. En caso negativo el programa
#no realiza ninguna acción. El programa también debe manejar los erro-
#res por intento de acceso incorrecto al diccionario y otros que puedan
#surgir utilizando una clave incorrecta.



d = {}
loop = true

while(loop):
	print("Ingrese el numero de la opcion para editar el diccionario creado")
	opcion = int(input("1 : Insertar entrada   2 : Eliminar entrada   3 : Modificar entrada"))

	if(opcion == 1):
		try:
			clave = input("Ingrese la clave de la entrada que desea ingresar al diccionario: ")
			valor = input("Ingrese el valor correspondiente a la clave recien ingresada: ")
			