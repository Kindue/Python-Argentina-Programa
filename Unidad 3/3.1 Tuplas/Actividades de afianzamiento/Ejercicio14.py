#Ejercicio 14
#Escriba un programa que permita que el usuario ingrese una
#tupla t y un elemento e. El programa debe informar si e está en la tupla
#t.


n = int(input("Ingrese la cantidad de elementos en la tupla t: "))

t = ()
for i in range(n):
	ele = input("Ingrese un elemento a la tupla: ")
	t += (ele,)

a = input("Ingrese el elemento a buscar en la tupla: ")

if(a in t):
	print("El elemento esta en la tupla")