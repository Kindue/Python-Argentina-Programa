#Ejercicio 11
#Defina la función porcentaje la cual recibe como parámetro
#una lista de números flotantes l y un número entero p. La función
#retorna como resultado el porcentaje p de la suma de los elementos de
#l. La función recibe como parámetro por defecto la lista vacía.


def porcentaje(lista, p):
	suma = 0
	for i in lista:
		suma += i
	return ((suma * p) / 100)

loop = True
l = []
while(loop):
	try:
		print("Ingrese un flotante para agregar a la lista, ingrese 0 para terminar de agregar")
		flotante = float(input())
		if(flotante == 0):
			loop = False
		else:
			l.append(flotante)
	except ValueError:
		print("El dato ingresado no es valido, intentelo de nuevo!")


loop = True
while(loop):
	try:
		print("Ingrese el porcentaje a calcular a la suma de los numeros de la lista ingresada:")
		p = int(input())
		loop = False
	except ValueError:
		print("El porcentaje ingresado no es un entero, intentelo de nuevo!")

print("Este es el", p,"% de la suma de los numeros de la lista ingresada:")
print(porcentaje(l, p))

