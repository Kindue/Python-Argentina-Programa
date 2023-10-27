#Ejercicio 8
#Construya un programa que permita que el usuario ingrese una
#dupla y luego desempaquete la tupla en dos variables a y b. Luego el
#programa debe imprimir las variables a y b.


t = ()
for i in range(2):
	ele = input("Ingrese un elemento para agregar a la tupla: ")
	t += (ele,)

print("Esta es mi dupla:", t)

a, b = t

print("El primer elemento de la dupla ahora es mi variable a:", a)
print("El segundo elemento de la dupla ahora es mi variable b:", b)

print("Mi dupla no cambio:", t)