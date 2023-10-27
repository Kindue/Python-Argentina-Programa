#Ejercicio 14
#Escriba un programa que permita que el usuario ingrese un
#número a y una lista l. Luego el programa debe mostrar por pantalla
#la cantidad de veces que aparece el número a en la lista l.


l = []
n = int(input("Ingrese la cantidad de numeros que quiere ingresar en la lista: "))
for i in range(n):
	num = int(input("Ingrese un numero para agregar a la lista: "))
	l.append(num)

a = int(input("Ingrese el numero a buscar cuantas veces aparece en la lista: "))

print("El numero", a, "aparece", l.count(a), "veces")