#Ejercicio 11
#Escriba un programa que permita que el usuario ingrese por
#teclado una lista l. El programa debe crear dos listas la lista vocales y la
#lista consonantes. En la lista vocales se encuentran todas la vocales que
#están en s y en la lista consonante todas las consonantes que están en
#s. Luego el programa debe imprimir por pantalla la cantidad de vocales
#y la cantidad de consonantes que tiene s.


l = []

vocales = {'A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú'}
consonantes = {'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z', 'W', 'Y'}

listaDeVocales = []
listaDeConsonantes = []

contVocales = 0
contConsonantes = 0

n = int(input("Ingrese la cantidad de strings que quiere ingresar en la lista: "))
for i in range(n):
	ele = input("Ingrese un string para agregar a la lista: ")
	l.append(ele)
	for j in ele:
		if(j.upper() in consonantes):
			contConsonantes += 1
			listaDeConsonantes.append(j)
		if(j.upper() in vocales):
			contVocales += 1
			listaDeVocales.append(j)


print("Este es el listado con todas las vocales en la lista ingresada:", listaDeVocales)
print("Se registraron", contVocales, "vocales en la lista ingresada")
print()
print("Este es el listado con todas las consonantes en la lista ingresada", listaDeConsonantes)
print("Se registraron", contConsonantes, "consonantes en la lista ingresada")