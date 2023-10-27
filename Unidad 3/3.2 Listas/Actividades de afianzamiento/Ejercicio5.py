#Ejercicio 5
#Escriba un programa que dada una lista t con 5 elementos y
#un número n produzca como resultado una nueva lista con todos los
#elementos de la lista t multiplicados por el número n.

print("Ingrese los cinco elementos que conforman la lista a multiplicar:")
t = []
for i in range(5):
	ele = int(input())
	t.append(ele)

print("La lista que se creo es la siguiente:", t)
n = int(input("Ingrese un numero para multiplicar la lista conformada: "))
lista_nueva = []
for i in range(5):
	lista_nueva.append(t[i] * n)


print("La lista resultante es la siguiente:", lista_nueva)