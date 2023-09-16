# Ejercicio 7: Defina la función recursiva esPotencia(n, b) la cual recibe 2
# enteros, n y b, y devuelve True si n es potencia de b y False en caso
# contrario.
# esPotencia(8, 2) −> True
# esPotencia(64, 4) −> True
# esPotencia(70, 10) −> False
# esPotencia(1, 2) −> True

def esPotencia(n, b):
	return esPotenciaAux(n, b)

def esPotenciaAux(n, b):
	if(n == 1):
		return True
	if(n == 0):
		return False
	return esPotenciaAux(n / b, b)
	 
try:
	print("Ingrese un numero para saber si es potencia de otro:")
	num = int(input())
	print("Ingrese la base para saber si el primer numero es potencia de la base:")
	base = int(input())
except ValueError():
	print("No ingreso un numero, adios!")

if(num < 0):
	print("Debe ingresar un numero positivo!")
else:
	if(esPotenciaAux(num, base)):
		print(num, "es potencia de", base)
	else:
		print(num, "NO es potencia de", base)

		 