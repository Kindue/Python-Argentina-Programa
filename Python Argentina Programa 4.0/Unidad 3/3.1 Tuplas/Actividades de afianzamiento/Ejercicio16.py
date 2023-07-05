#Ejercicio 16
#Escriba un programa que permita que el usuario ingrese dos
#tuplas t y r. El programa debe imprimir por pantalla la concatenación
#de t y r.


n = int(input("Ingrese la cantidad de elementos en la tupla t: "))

t = ()
for i in range(n):
	ele = input("Ingrese un elemento a la tupla: ")
	t += (ele,)

n = int(input("Ingrese la cantidad de elementos en la tupla r: "))

r = ()
for i in range(n):
	ele = input("Ingrese un elemento a la tupla: ")
	r += (ele,)

concatenacion = t + r

print("t y r concatenados forman la siguiente tupla:", concatenacion)