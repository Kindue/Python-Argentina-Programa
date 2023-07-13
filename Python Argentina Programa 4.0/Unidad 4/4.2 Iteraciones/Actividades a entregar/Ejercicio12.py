#Ejercicio 12
#Escriba un programa que permita que el usuario ingrese por
#teclado una lista de strings. El programa retorna como resultado la
#misma lista pero con los strings invertidos.


l = []
n = int(input("Ingrese la cantidad de strings que quiere ingresar en la lista: "))
for i in range(n):
	ele = input("Ingrese un string para agregar a la lista: ")
	l.append(ele)

print("Esta es la lista de strings ingresada sin invertir sus elementos:", l)

for i in range(len(l)):
	l[i] = l[i][::-1]

print("Esta es la lista de strings ingresada ahora con sus elementos invertidos:", l)
