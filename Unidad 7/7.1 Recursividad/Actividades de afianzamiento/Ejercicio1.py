# Ejercicio 1: Implemente la función factorial la cual se define como sigue:
# factorial(n)=
# 1 si n=0
# n* factorial(n-1) si n >0


def factorial(n):
	return factorialAux(n)

def factorialAux(n):
	if(n == 1) or (n == 0):
		return 1
	else:
		return n * factorialAux(n-1)
	
try:
    print("Ingrese un numero para calcular su factorial:")
    num = int(input())
except ValueError():
	print("No ingreso un numero, adios!")
	
if(num < 0):
	print("Debe ingresar un numero positivo!")
else:
	print("El factorial de", num, "es el siguiente")
	print(f"{num}! = {factorial(num)}")
	