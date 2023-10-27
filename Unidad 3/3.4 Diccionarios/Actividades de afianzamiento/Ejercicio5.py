#Ejercicio 5
#Escriba un programa que:
#1. Permita que el usuario ingrese un diccionario d.
#2. Permita que el usuario ingrese una clave c.
#3. Imprima por pantalla si la clave c está en el diccionario d.


d = {}
entrada = input("Ingrese los elementos del diccionario, separando cada elemento con un espacio y en cada elemento separar la clave y el valor con una coma: ").split()

for i in range(len(entrada)):
	elemento = entrada[i].split(",")
	d[elemento[0]] = elemento[1]

clave = input("Ingrese una clave a buscar en el diccionario: ")

if(clave in d):
	print("La clave esta en el diccionario")
else:
	print("La clave no esta en el diccionario")