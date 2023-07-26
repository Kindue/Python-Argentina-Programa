#Ejercicio 2
#Realice las siguientes actividades:
#1. Defina la función pares la cual recibe como parámetro una lista de
#números enteros l y retorna como resultado una lista que contiene
#los números pares l.
#2. Defina la función impares la cual recibe como parámetro una lis-
#ta de números enteros l y retorna como resultado una lista de
#números impares.
#3. Defina la función mayoría la cual recibe como parámetro dos listas
#de números enteros, una que contiene números pares y otra que
#contiene números impares. La función informa si hay mayoría de
#números pares o mayoría de números impares o no hay igualdad
#de números pares e impares.
#4. Construya un programa principal que:
#a) Permita que el usuario ingrese una lista de números enteros.
#b) Informe si la lista tiene mayoría de pares o mayoría de impares
#o tiene la misma cantidad de pares que impares.


def pares(lista):
	l = []
	for i in lista:
		if(i % 2 == 0):
			l.append(i)
	return l

def impares(lista):
	l = []
	for i in lista:
		if(i % 2 != 0):
			l.append(i)
	return l

def hayMayoria(lista1, lista2):
	aRet = 0
	if(len(lista1) == len(lista2)):
		aRet = 0
	elif(len(lista1) > len(lista2)):
		aRet = 1
	else:
		aRet = -1
	return aRet

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
	loop = True
	while (loop):
		try:
			num = int(input("Ingrese un numero a la lista: "))
			l.append(num)
			loop = False
			print("--"*40)
		except ValueError:
			print("Ingreso un simbolo no valido, por favor intente ingresar un numero de nuevo!")

resultado = hayMayoria(pares(l), impares(l))

print()
print("--"*40)
print()

if(resultado == 0):
	print("La lista que ingreso tiene igual cantidad de pares y de impares!")
elif(resultado == 1):
	print("La lista que ingreso tiene mas pares que impares!")
else:
	print("La lista que ingreso tiene mas impares que pares!")