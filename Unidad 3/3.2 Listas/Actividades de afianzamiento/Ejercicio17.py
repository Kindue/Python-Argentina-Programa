#Ejercicio 17 
#Escriba un programa que:
#1. Permita que el usuario ingrese una lista l.
#2. Pida al usuario en elemento e.
#3. Pida al usuario una posición p válida.
#4. Inserte en la lista l el elemento e en la posición p.


l = []
n = int(input("Ingrese la cantidad de elementos que quiere ingresar en la lista: "))
for i in range(n):
	ele = input("Ingrese un elemento para agregar a la lista: ")
	l.append(ele)


ele = input("Ingrese un elemento a insertar: ")

pos = int(input(f"Ingrese un numero del 0 al {(n-1)} que sera la posicion a insertar el elemento en la lista: "))

l.insert(pos, ele)


print()
print("Mi nueva lista es la siguiente:", l)