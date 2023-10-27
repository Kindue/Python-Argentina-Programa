#Ejercicio 6:
#Escriba un programa que:
#1. Permita que el usuario ingrese cuatro números, los almacene una
#tupla t.
#2. Genere una tupla s la cual se obtiene sumando a cada elemento
#de t un valor ingresado por el usuario.
#3. Genere una tupla r la cual se obtiene restando a cada elemento de
#t un valor ingresado por el usuario.
#4. Imprima: con leyendas adecuadas la tupla t, s y r.


t = ()
for i in range(4):
	num = int(input("Ingrese un numero para agregar a la tupla: "))
	t += (num,)


n = int(input("Ingrese un numero para sumar los elementos de la tupla: "))
s = ()

for i in range(4):
	s += (t[i] + n,)


p = int(input("Ingrese un numero para restar los elementos de la tupla: "))
r = ()

for i in range(4):
	r += (t[i] - p,)



print()
print("Esta es la tupla original t:", t)
print("Esta es la tupla obtenida al sumar los elementos de t:", s)
print("Esta es la tupla obtenida al restar los elementos de t:", r)