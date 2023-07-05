#Ejercicio 9
#Escriba un programa que permita que el usuario ingrese un
#conjunto c y un valor v y si v está en c lo elimine de c. Luego imprima
#c.


A = set()
n = int(input("Ingrese la cantidad de elementos que desee ingresar al conjunto: "))
for i in range(n):
	ele = input("Ingrese un elemento al conjunto: ")
	A.add(ele)


v = input("Ingrese un valor v a buscar en el conjunto y eliminarlo: ")

if(v in A):
	A.remove(v)
	print("Este es el conjunto luego de remover el valor ingresado:", A)
else:
	print("No se encontro el valor, no se ha removido nada:", A)