#Ejercicio 10
#Escriba un programa que permite que el usuario ingrese un
#número a y una tupla t. Luego el programa debe imprimir True si el
#número a está en t y False en otro caso.


n = int(input("Ingrese la cantidad de elementos en la tupla t: "))

t = ()
for i in range(n):
	num = int(input("Ingrese un numero a la tupla: "))
	t += (num,)

a = int(input("Ingrese el numero a buscar en la tupla: "))

print(a in t)