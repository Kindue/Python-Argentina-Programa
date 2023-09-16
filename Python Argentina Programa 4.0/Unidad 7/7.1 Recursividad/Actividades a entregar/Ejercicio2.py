# Ejercicio 2: Implemente una función que permita obtener el n-ésimo núme-
# ro de la sucesión de fibonacci. La sucesión de fibonacci se define como
# sigue:
# fibonacci(n)=
# 0 si n=0
# 1 si n=1
# fibonacci(n −1)+fibonacci(n −2)si n >2

def fibonacci(n):
	return fibonacciAux(n)

def fibonacciAux(n):
	if(n == 0):
		return 0
	elif(n == 1):
		return 1
	else:
		return fibonacciAux(n-1) + fibonacciAux(n-2)
	

try:
    print("Ingrese un numero para calcular el numero de Fibonacci")
    print("Tenga en cuenta que para numeros mayores a 30 el programa puede tardar!")
    num = int(input())
except ValueError():
	print("No ingreso un numero, adios!")
	
if(num < 0):
	print("Debe ingresar un numero positivo!")
else:
	print("El numero de fibonacci correspondiente a", num, "es el siguiente")
	print(f"F({num}) = {fibonacci(num)}")