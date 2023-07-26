#Ejercicio 1
#Defina la función sumaPar la cual recibe como parámetro una
#lista l de números enteros y produce como resultado la suma de los
#números pares que se encuentran en l. Luego construya un programa
#principal que:
#Permita que el usuario ingrese una lista de números enteros.
#Imprima la suma de los números pares que se encuentran en la
#lista.


def sumaPar(lista):
	suma = 0
	for i in range(len(lista)):
		suma += i
	return suma

l = []
loop = True
while (loop):
	try:
		n = int(input("Ingrese la cantidad de numeros que desea insertar en la lista: "))
		loop = False
	except ValueError:
		print("Ingreso un simbolo no valido, por favor intentelo de nuevo")

for k in range(n):
	loop = True
	while (loop):
		try:
			num = int(input("Ingrese un numero a la lista: "))
			l.append(num)
			loop = False
		except ValueError:
			print("Ingreso un simbolo no valido, por favor intente ingresar un numero de nuevo!")


print()
print("La suma de los numeros de la lista ingresada es la siguiente: ", sumaPar(l))

