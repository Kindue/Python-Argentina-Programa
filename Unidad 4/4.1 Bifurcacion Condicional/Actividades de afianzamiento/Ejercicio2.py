#Ejercicio 2
#Escriba un programa que permita que el usuario ingrese un
#número n. El programa debe informar si el número es capicúa o no.


numero = input("Ingrese un numero para saber si es capicua: ")

numero_revertido = numero[-1::-1]

if(numero == numero_revertido):
	print("El numero es capicua!")
else:
	print("El numero no es capicua!")