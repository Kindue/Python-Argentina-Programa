#Ejercicio 4
#Escriba un programa que a partir de dos conjuntos de números
#enteros ingresados por el usuario cree el conjunto universal el cual está
#formado por todos los números que pertenecen a los conjuntos usados
#en el programa.


A = set()
n = int(input("Ingrese la cantidad de numeros enteros que desea ingresar en el conjunto A: "))
for i in range(n):
	num = int(input("Ingrese un numero al conjunto A: "))
	A.add(num)

B = set()
k = int(input("Ingrese la cantidad de numeros enteros que desea ingresar en el conjunto B: "))
for it in range(k):
	num = int(input("Ingrese un numero al conjunto B: "))
	B.add(num)


conj_universal = A.union(B)

print("Los numeros del conjunto universal formado por la union de los dos conjuntos ingresados son los siguientes:")
print(conj_universal)