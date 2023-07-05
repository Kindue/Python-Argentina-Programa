#Ejercicio 6
#Escriba un programa que permita que el usuario ingrese un dic-
#cionario. El programa debe imprimir una lista de tuplas donde en cada
#tupla tiene como primer elemento la clave y como segundo elemento el
#valor asociado a la clave.


d = {}
entrada = input("Ingrese los elementos del diccionario, separando cada elemento con un espacio y en cada elemento separar la clave y el valor con una coma: ").split()

for i in range(len(entrada)):
	elemento = entrada[i].split(",")
	d[elemento[0]] = elemento[1]

lista_de_tuplas = []
for i in d.items():
	lista_de_tuplas.append(i)


print("La lista de tuplas creada con el diccionario ingresado es la siguiente:")
print(lista_de_tuplas)
