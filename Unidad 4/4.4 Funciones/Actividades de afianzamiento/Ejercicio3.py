#Ejercicio 3 
#Escriba una función que reciba como parámetros una lista de
#strings. La función crea un diccionario cuya clave son las letras del
#string y cuyo valor la cantidad de veces que aparece la clave en la
#lista de string. Luego escriba un programa principal que permita que
#el usario ingrese una lista de string e imprima el diccionario resultante
#de aplicar la función a la lista ingresada por el usuario.


def diccionario(lista):
	dic = {}
	for c in lista:
		if(c not in dic):
			dic[c] = contador(c, lista)
	return dic

def contador(caracter, lista):
	contador = 0
	i = lista.index(caracter)
	for i in range(len(lista)):
		if(l[i] == caracter):
			contador += 1
	return contador


l = []
loop = True
while (loop):
	try:
		n = int(input("Ingrese la cantidad de numeros que desea insertar en la lista: "))
		loop = False
		print("--"*40)
	except ValueError:
		print("Ingreso un simbolo no valido, por favor intentelo de nuevo")

for k in range(n):
	char = str(input("Ingrese un caracter para agregar a la lista: "))
	l.append(char)

print()
print("--"*40)
print()
print("El diccionario creado a partir de la lista ingresada es el siguiente:")
print(diccionario(l))