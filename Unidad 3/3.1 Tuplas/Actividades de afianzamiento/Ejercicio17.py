#Ejercicio 17
#Escriba un programa que:
#1. Permita que el usuario ingrese una tupla t de cinco números.
#2. Sume los números pares.
#3. Sume los números impares.


t = ()
sumaI = 0
sumaP = 0
for i in range(5):
	num = int(input("Ingrese un numero a la tupla: "))
	t += (num,)
	if(num % 2 == 0):
		sumaP = sumaP + num
	else:
		sumaI = sumaI + num

print("La suma de los numeros pares de la tupla da como resultado", sumaP)
print()
print("La suma de los numeros impares de la tupla da como resultado", sumaI)
