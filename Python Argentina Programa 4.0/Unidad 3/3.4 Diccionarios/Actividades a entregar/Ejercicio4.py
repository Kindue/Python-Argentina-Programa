#Ejercicio 4
#Escriba un programa que:
#1. Permita que el usuario ingrese un diccionario d.
#2. Permita que el usuario ingrese un elemento e.
#3. Cuente cuántas veces aparece e en los valores de d.


d = {}
n = int(input("Ingrese la cantidad de elementos que desee insertar en el diccionario a: "))
for i in range(n):
	clave = input("Ingrese una clave: ")
	valor = input("Ingrese su valor asociado: ")
	d[clave] = valor

e = input("Ingrese un valor e a buscar en el diccionario: ")

suma = 0
for v in d.values():
	if(v == e):
		suma = suma + 1


print("El valor e aparece en el diccionario", suma, "veces")