#Ejercicio 11
#Escriba un programa que permita que el usuario ingrese un
#número a y una lista l. Luego el programa debe imprimir True si el
#número a está en l y False en otro caso.


l = []
n = int(input("Ingrese la cantidad de numeros que quiere ingresar en la lista: "))
for i in range(n):
	num = int(input("Ingrese un numero para agregar a la lista: "))
	l.append(num)

a = int(input("Ingrese el numero a buscar en la lista: "))

print(a in l)