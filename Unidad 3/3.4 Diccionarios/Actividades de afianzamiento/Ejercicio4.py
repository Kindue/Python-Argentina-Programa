#Ejercicio 4
#Escriba un programa que:
#1. Permita que el usuario ingrese un diccionario d.
#2. Permita que el usuario ingrese un elemento e.
#3. Cuente cuántas veces aparece e en los valores de d.


entrada = input("Ingrese los elementos del diccionario, separando cada elemento con un espacio y en cada elemento separar la clave y el valor con una coma: ").split()

e = input("Ingrese un valor e a buscar en el diccionario: ")

d = {}
for i in range(len(entrada)):
	elemento = entrada[i].split(",")
	d[elemento[0]] = elemento[1]

suma = 0
for v in d.values():
	if(v == e):
		suma = suma + 1


print("El valor e aparece en el diccionario", suma, "veces")