#Ejercicio 16
#Construya un programa que:
#1. Permita que el usuario ingrese una lista l de números enteros l.
#2. Ordene la lista
#3. Almacene en la variable mayor el mayor elemento de la lista
#4. Almacene en la variable menor el menor elemento de la lista.
#5. Imprima por pantalla la lista l y el elemento mayor y el elemento
#menor.


l = []
n = int(input("Ingrese la cantidad de numeros que quiere ingresar en la lista: "))
for i in range(n):
	num = int(input("Ingrese un numero para agregar a la lista: "))
	l.append(num)

l.sort()

mayor = l[-1]
menor = l[0]

print("La lista ingresada es la sguiente:", l)
print()
print("El mayor numero de la lista es:", mayor)
print()
print("El menor numero de la lista es:", menor)