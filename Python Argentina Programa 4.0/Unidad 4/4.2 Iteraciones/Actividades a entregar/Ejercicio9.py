#Ejercicio 9
#Escriba un programa que permita que el usuario ingrese n
#strings. El programa debe imprimir por pantalla el string de mayor
#longitud.


n = int(input("Ingrese la cantidad de strings que desee ingresar: "))

stringMasLargo = ''

for i in range(n):
	string = input("Ingrese un string: ")
	if(len(string) > len(stringMasLargo)):
		stringMasLargo = string


print("El string mas largo ingresado es:", stringMasLargo)