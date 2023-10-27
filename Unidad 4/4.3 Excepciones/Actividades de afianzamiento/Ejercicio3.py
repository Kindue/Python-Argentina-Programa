#Ejercicio 3
#Escriba un programa que permita que el usuario ingrese una
#lista de elementos. El programa debe sumar los elementos numéricos
#que se encuentran en la lista. Cuando el programa encuentra un
#elemento que no es numérico dispara una excepción ValueError la cual
#tiene un manejador que inserta el elemento que provocó la excepción
#en una lista de elementos no numéricos.



lista = []
loop = True
while(loop):
	print("Ingrese un elemento a la lista o escriba 'Finalizar' para conocer la suma de los elementos numericos de la lista:")
	ele = input()
	if(ele.upper() == "FINALIZAR"):
		loop = False
	else:
		lista.append(ele)

noNumericos = []
suma = 0

for ele in lista:
	try:
		ele = int(ele)
	except ValueError:
		noNumericos.append(ele)
	else:
		suma = suma + ele
	finally:
		print("Lista parcial de elementos no numericos:")
		print(noNumericos)
		print("Suma parcial de elementos numericos:")
		print(suma)

print("Lista final de elementos no numericos:")
print(noNumericos)
print("Suma final de elementos numericos:")
print(suma)