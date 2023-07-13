#Ejercicio 7
#Escriba un programa que permita que el usuario ingrese por
#teclado un string s. El programa deberá contar la cantidad de vocales
#y consonantes que tiene s.


string = input("Ingrese una cadena de caracteres para contar cuantas consonantes y cuantas vocales tiene: ")

vocales = {'A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú'}
consonantes = {'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z', 'W', 'Y'}

contVocales = 0
contConsonantes = 0

for i in string:
	if(i.upper() in consonantes):
		contConsonantes += 1
	if(i.upper() in vocales):
		contVocales += 1


print("La cantidad de vocales en la cadena de caracteres ingresada es:", contVocales)
print()
print("La cantida de consonantes en la cadena de caracteres ingresada es:", contConsonantes) 