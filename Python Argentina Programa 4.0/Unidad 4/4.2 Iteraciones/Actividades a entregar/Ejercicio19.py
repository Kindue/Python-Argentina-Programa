#Ejercicio 19
#Cree un diccionario cuya clave sea un número y cuyo valor
#sea un string. Tanto la clave como el valor son requeridos al usuario.
#Luego el diccionario debe imprimir la clave que tenga como valor el
#string más largo.


d = {}
n = int(input("Ingrese la cantidad de entradas que quiere agregar al diccionario: "))

for i in range(n):
	numero = int(input("Ingrese un numero para representar la clave de la entrada: "))
	string = input("Ingrese un string para representar el valor de la entrada: ")
	d[numero] = string

mayorValor = ''

for e in d.keys():
	if(len(d[e]) > len(mayorValor)):
		mayorValor = d[e]
		mayorClave = e


print("La clave que le corresponde al string mas largo es", mayorClave)
print("Su string es el siguiente:", d[mayorClave])