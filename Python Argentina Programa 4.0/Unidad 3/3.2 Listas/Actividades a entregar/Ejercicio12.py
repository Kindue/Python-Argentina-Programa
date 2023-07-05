#Ejercicio 12
#Escriba un programa que permita que el usuario ingrese un
#número a y una lista l. Luego el programa debe imprimir por pantalla
#la posición del número a en la lista l. En caso de que el número a no se
#encuentre en l el programa debe imprimir -1.


l = []
n = int(input("Ingrese la cantidad de numeros que quiere ingresar en la lista: "))
for i in range(n):
	num = int(input("Ingrese un numero para agregar a la lista: "))
	l.append(num)

a = int(input("Ingrese el numero a buscar su indice en la lista: "))

if(a in l):
	print("El indice del numero ingresado en la lista creada anteriormente es: ", l.index(a))
else:
	print("-1")