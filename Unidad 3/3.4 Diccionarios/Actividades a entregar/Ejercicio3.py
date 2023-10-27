#Ejercicio 3
#Escriba un programa que permita que el usuario ingrese una
#lista de duplas ln. Cada dupla tiene como primer componente un nom-
#bre y como segunda componente un número. Luego cree un diccionario
#cuyas claves son los nombres en ln y cuyo valor sean enteros.


lista = []
n = int(input("Ingrese la cantidad de duplas que desee insertar en la lista: "))
for i in range(n):
	print("Ingrese el nombre y el numero de una dupla")
	nombre = input("Ingrese el nombre: ")
	numero = int(input("Ingrese el numero: "))
	lista.append((nombre, numero))

d = {}
for i in lista:
	d[i[0]] = i[1]

print("El diccionario creado es el siguiente:", d)