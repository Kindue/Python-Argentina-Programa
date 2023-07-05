#Ejercicio 10
#Escriba un programa que:
#1. Permita que el usuario ingrese un conjunto A.
#2. Permita que el usuario ingrese un conjunto B.
#3. Informe si A es un subconjunto de B o B es un subconjunto de A.


A = set()
n = int(input("Ingrese la cantidad de elementos que desee ingresar al conjunto A: "))
for i in range(n):
	ele = input("Ingrese un elemento al conjunto A: ")
	A.add(ele)

B = set()
k = int(input("Ingrese la cantidad de elementos que desee ingresar en el conjunto B: "))
for it in range(k):
	ele = input("Ingrese un numero al conjunto B: ")
	B.add(ele)

if(A <= B):
	print("El conjunto A es un subconjunto del conjunto B")

if(B <= A):
	print("El conjunto B es un subconjunto del conjunto A")

if(not(B <= A) and not(A <= B)):
	print("Ninguno de los dos conjuntos es un subconjunto del otro")