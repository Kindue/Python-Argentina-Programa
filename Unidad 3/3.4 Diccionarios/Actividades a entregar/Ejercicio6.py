#Ejercicio 6
#Escriba un programa que permita que el usuario ingrese un dic-
#cionario. El programa debe imprimir una lista de tuplas donde en cada
#tupla tiene como primer elemento la clave y como segundo elemento el
#valor asociado a la clave.


d = {}
n = int(input("Ingrese la cantidad de elementos que desee insertar en el diccionario a: "))
for i in range(n):
	clave = input("Ingrese una clave: ")
	valor = input("Ingrese su valor asociado: ")
	d[clave] = valor

lista_de_tuplas = []
for i in d.items():
	lista_de_tuplas.append(i)


print("La lista de tuplas creada con el diccionario ingresado es la siguiente:")
print(lista_de_tuplas)
