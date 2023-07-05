#Ejercicio 6
#Escriba un programa que permita que el usuario ingrese un
#conjunto y un valor. El programa debe informar si valor pertenece a
#conjunto.


A = set()
n = int(input("Ingrese la cantidad de elementos que desee ingresar al conjunto: "))
for i in range(n):
	ele = input("Ingrese un elemento al conjunto: ")
	A.add(ele)

valor = input("Ingrese un elemento a buscar en el conjunto: ")

if(valor in A):
	print("El valor ingresado", valor, "esta en el conjunto ingresado")
else:
	print("El valor ingresado", valor, "no esta en el conjunto ingresado")