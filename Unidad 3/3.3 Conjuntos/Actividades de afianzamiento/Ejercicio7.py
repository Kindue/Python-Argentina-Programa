#Ejercicio 7
#Escriba un programa que permita que el usuario ingrese un
#conjunto y tres valores. El programa debe incorporar esos valores al
#conjunto. Luego imprimir el conjunto resultado por pantalla.


A = set()
n = int(input("Ingrese la cantidad de elementos que desee ingresar al conjunto: "))
for i in range(n):
	ele = input("Ingrese un elemento al conjunto: ")
	A.add(ele)

for i in range(3):
	valor = input("Ingrese un valor a incorporar al conjunto: ")
	A.add(valor)

print("El conjunto resultante es el siguiente:", A)