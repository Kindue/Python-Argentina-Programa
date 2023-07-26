#Ejercicio 14
#Escriba un programa que permita que el usuario ingrese dos
#diccionarios a y b y a partir de ellos cree las siguientes vistas:
#1. u el cual contiene la unión de la vista de claves de a con la vista
#de claves de b.
#2. i el cual contiene la intersección de la vista de claves de a con la
#vista de claves de b.
#3. d la cual contiene la diferencia entre la vista de claves de a con la
#vista de claves de b.
#4. ds la cual contiene la diferencia simétrica de la visa de claves de a
#con la vista de claves de b.


a = {}
n = int(input("Ingrese la cantidad de elementos que desee insertar en el diccionario a: "))
for i in range(n):
	clave = input("Ingrese una clave: ")
	valor = input("Ingrese su valor asociado: ")
	a[clave] = valor

b = {}
k = int(input("Ingrese la cantidad de elementos que desee insertar en el diccionario b: "))
for i in range(k):
	clave = input("Ingrese una clave: ")
	valor = input("Ingrese su valor asociado: ")
	b[clave] = valor

a_aux = set(a.keys())
b_aux = set(b.keys())

u = a_aux.union(b_aux)
print("La union de las claves de a con las claves de b forman el siguiente conjunto")
print(u)
print()

i = a_aux.intersection(b_aux)
print("La interseccion de las claves de a con las claves de b forman el siguiente conjunto")
print(i)
print()

d = a_aux.difference(b_aux)
print("La claves que estan en a y que no estan en b son las siguientes:")
print(d)
print()

ds = a_aux.symmetric_difference(b_aux)
print("Las claves que estan en a y b pero no estan en ambos diccionarios son las siguientes:")
print(ds)
print()

