#Ejercicio 8
#Escriba un programa que:
#1. Almacene una contraseña en una variable.
#2. Pregunte al usuario por la contraseña.
#3. Imprima por pantalla si la contraseña introducida por el usua-
#rio coincide con la guardada en la variable sin tener en cuenta
#mayúsculas y minúsculas.



loop = True
while(loop):
	contraseña = 'qwerty'
	entrada = input("Ingrese la contraseña: ")

	if(contraseña == entrada):
		print("Contraseña correcta, bienvenido Agente 47")
		opcion = input("Ingrese 0 para salir: ")
	else:
		print("Contraseña incorrecta, intente de nuevo")
		opcion = input("Ingrese 0 para salir o cualquier otra tecla para volver a intentar: ")

	if(opcion == '0'):
		loop = False