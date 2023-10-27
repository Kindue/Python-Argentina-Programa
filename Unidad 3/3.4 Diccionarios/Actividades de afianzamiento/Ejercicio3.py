#Ejercicio 3
#Escriba un programa que permita que el usuario ingrese una
#lista de duplas ln. Cada dupla tiene como primer componente un nom-
#bre y como segunda componente un número. Luego cree un diccionario
#cuyas claves son los nombres en ln y cuyo valor sean enteros.


ln = input("Ingrese la lista de duplas separando cada dupla con un espacio y cada elemento de la dupla separado por una coma:").split()

d = {}
for i in range(len(ln)):
	dupla = ln[i].split(",")
	d[dupla[0]] = dupla[1]


print(d)