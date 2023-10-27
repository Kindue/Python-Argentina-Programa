#Ejercicio 9
#Construya un programa que permita que el usuario ingrese una
#lista de dos elementos y luego desempaquete la lista en dos variables a
#y b. Luego el programa debe imprimir las variables a y b.


lista = []
print("Ingrese el primer elemento de la lista: ")
lista.append(input())

print("Ingrese el segundo elemento de la lista: ")
lista.append(input())

a, b = lista

print("La variable a es el primer elemento de la lista:", a)
print("La variable b es el segundo elemento de la lista:", b)
