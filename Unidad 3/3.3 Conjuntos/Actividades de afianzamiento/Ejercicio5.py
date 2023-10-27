#Ejercicio 5
#Escriba un programa que:
#1. Ingrese un conjunto.
#2. Imprima por pantalla: la cardinalidad, el mínimo y el máximo.


A = set()
n = int(input("Ingrese la cantidad de elementos que desee ingresar al conjunto: "))
for i in range(n):
	ele = input("Ingrese un elemento al conjunto: ")
	A.add(ele)

print("La cardinalidad del conjunto es:",len(A))
print()
print("El minimo elemento en el conjunto es", min(A))
print()
print("El maximo elemento en el conjunto es", max(A))