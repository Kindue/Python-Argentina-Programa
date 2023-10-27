#Ejercicio 7
#Escriba un programa que:
# 1. Permita que el usuario ingrese cuatro números, los almacene una
#lista l.
# 2.Genere una lista s la cual se obtiene sumando a cada elemento de
#l un valor ingresado por el usuario.
# 3.Genere una lista r la cual se obtiene restando a cada elemento de
#l un valor ingresado por el usuario.
# 4.Imprima: con leyendas adecuadas la tupla l, s y r.


print("Ingrese los cuatro numeros para crear la lista l y realizar operaciones: ")
l = []
for i in range(4):
	ele = int(input())
	l.append(ele)

sNum = int(input("Ingrese un valor para sumar los elementos de la lista l: "))
s = []
for i in range(4):
	sumaEle = l[i] + sNum
	s.append(sumaEle)

rNum = int(input("Ingrese un valor para restar los elementos de la lista l: "))
r = []
for i in range(4):
	restaEle = l[i] - rNum
	r.append(restaEle)

print("Asi quedo la lista original l:", l)
print("Asi quedo la lista s al sumar los elementos de l", s)
print("Asi quedo la lista r al restar los elementos de l:", r)