#Ejercicio 11
#Escriba un programa que permita que el usuario ingrese un
#número a y una tupla t. Luego el programa debe imprimir por pantalla
#la posición del número a en la tupla t. En caso de que el número a no
#se encuentre en t el programa debe imprimir -1.


n = int(input("Ingrese la cantidad de elementos en la tupla t: "))

t = ()
for i in range(n):
	num = int(input("Ingrese un numero a la tupla: "))
	t += (num,)

a = int(input("Ingrese el numero a buscar en la tupla: "))

if(not(a in t)):
	print("-1")
else:
	print("La posicion del numero buscado en la tupla es: ", t.index(a))
