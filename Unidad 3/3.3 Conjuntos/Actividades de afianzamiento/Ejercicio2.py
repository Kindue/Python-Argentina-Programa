#Ejercicio 2
#Escriba un programa que:
#1. Defina el conjunto universal U el cual está compuesto por los nú-
#meros del 1 al 20.
#2. Pida al usuario dos conjuntos A y B.
#3. Calcule la unión de A y B.
#4. Calcule la intersección de A y B.
#5. Calcule el complemento de las unión e intersección de A y B.


U = frozenset({1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 , 14, 15, 16, 17, 18, 19, 20})

A = set()
n = int(input("Ingrese la cantidad de numeros que desee ingresar en el conjunto A: "))
for i in range(n):
	num = int(input("Ingrese un numero al conjunto A: "))
	A.add(num)

B = set()
k = int(input("Ingrese la cantidad de numeros que desee ingresar en el conjunto B: "))
for i in range(k):
	num = int(input("Ingrese un numero al conjunto B: "))
	B.add(num)

union = A.union(B)
print("La union de A y B es la siguiente", union)
print()

interseccion = A.intersection(B)
print("La interseccion de A y B es la siguiente", interseccion)
print()

complemento_union = set(U.difference(union))
print("El complemento de la union de A y B con respecto a nuestro conjunto universal es el siguiente:")
print(complemento_union)

complemento_interseccion = set(U.difference(interseccion))
print("El complemento de la interseccion de A y B con respecto a nuestro conjunto universal es el siguiente")
print(complemento_interseccion)