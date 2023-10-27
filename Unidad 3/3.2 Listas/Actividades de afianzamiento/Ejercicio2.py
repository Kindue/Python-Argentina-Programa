#Ejercicio 2
#Realice las siguientes actividades:
#1. Defina una lista l de tres números donde cada número es 0.
#2. Defina una lista de un único elemento.
#3. Defina una lista con n 0s.

n1 = n2 = n3 = 0
tres_ceros = [n1, n2, n3]
print("La lista con tres ceros fue creada, mire:")
print(tres_ceros)

unico_elemento = [420]
print("La lista con un unico elemento fue creada, mire")
print(unico_elemento)

n = int(input("Ingrese la cantidad de 0s que quiere poner en una lista: "))
lista_de_ceros = []
for i in range(n):
	lista_de_ceros.append(0)
print("La lista con", n, "ceros fue creada, mire:")
print(lista_de_ceros)