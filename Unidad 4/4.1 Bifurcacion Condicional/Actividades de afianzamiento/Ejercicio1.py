#Ejercicio 1
#Escriba un programa que permita que el usuario ingrese un
#número el programa debe informar si el número ingresado es par o
#impar.


numero = int(input("Ingrese un numero para saber si es par o impar: "))

if(numero % 2 == 0):
	print("El numero es par!")
else:
	print("El numero es impar!")