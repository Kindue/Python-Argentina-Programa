#Ejercicio 7
#Escriba un programa que permita almacenar en un diccionario
#tres personas. Por cada persona se registra: el dni, nombre, domicilio y
#edad. Use como clave para el diccionario el dni.


print("Ingrese los datos de tres personas para almacenarlas en un diccionario:")
diccionario = {}
for i in range(3):
	print("Ingrese los datos de una persona:")
	dni = int(input("Ingrese el DNI: "))
	nombre = input("Ingrese el nombre: ")
	domicilio = input("Ingrese el domicilio: ")
	edad = int(input("Ingrese su edad: "))
	datos = [nombre, domicilio, edad]
	diccionario[dni] = datos


print("El diccionario creado es el siguiente:")
print(diccionario)