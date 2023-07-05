#Ejercicio 11
#Escriba un programa que permita que el usuario ingrese un
#número a y una tupla t. Luego el programa debe insertar en el diccio-
#nario d el par a,t.


a = int(input("Ingrese un numero para representar una clave en el diccionario d: "))
t = ()
n = int(input("Ingrese la cantidad de elementos en la tupla t: "))
for i in range(n):
	ele = input("Ingrese un elemento a la tupla t: ")
	t += (ele,)

d = {}
d[a] = t

print()
print("El diccionario d es el siguiente:", d)