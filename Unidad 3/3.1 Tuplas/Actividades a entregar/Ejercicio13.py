#Ejercicio 13
#Escriba un programa que permita que el usuario ingrese un
#número a y una tupla t. Luego el programa debe mostrar por pantalla
#la cantidad de veces que aparece el número a en la tupla t.


n = int(input("Ingrese la cantidad de elementos en la tupla t: "))

t = ()
for i in range(n):
	num = int(input("Ingrese un numero a la tupla: "))
	t += (num,)

a = int(input("Ingrese el numero a contar la cantidad de veces que aparece en la tupla: "))

print("El numero buscado aparece", t.count(a), "veces")