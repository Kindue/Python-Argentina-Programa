#Ejercicio 12
#Implemente las siguientes funciones:
#Factorial(n)= 1 × 2 × 3 × ..... × n − 1 × n
#Fibonacci(n) la cual se define como sigue:
#• Fibonacci(0)=0
#• Fibonacci(1)=1
#• Fibonacci(n)=Fibonacci(n-1)+Fibonacci(n-2).
#Potencia(n,m)=nm
#Luego construya un programa principal que permita probar las
#funciones. Esto es invocarlas con argumentos correctos e incorrectos. Maneje
#los errores que surgen por la invocación de argumentos incorrectos con
#excepciones.



def factorial(n):
	return factorialAux(n)

def factorialAux(n):
	if(n == 1) or (n == 0):
		return 1
	else:
		return n * factorialAux(n-1)

def potencia(n, m):
	resultado = 1
	for i in range(m):
		resultado = resultado * n
	return resultado

def fibonacci(n):
	return fibonacciAux(n)

def fibonacciAux(n):
	if(n == 0):
		return 0
	elif(n == 1):
		return 1
	else:
		return fibonacciAux(n-1) + fibonacciAux(n-2)

loop = True
print("Bienvenido a la calculadora especializada")
while(loop):
	print("--"*40)
	print("Ingrese el numero de la opcion deseada")
	print("--"*40)
	print("1 : Factorial")
	print("--"*40)
	print("2 : Potencia")
	print("--"*40)
	print("3 : Fibonacci")
	print("--"*40)
	print("0 : Salir")
	print("--"*40)
	print()
	try:
		opcion = int(input())
	except ValueError:
		print("Ingreso una opcion invalida, por favor intentelo de nuevo!")
	else:
		if(opcion == 1):
			try:
				print("Ingrese un numero entero para calcular su factorial:")
				num = int(input())
				print("El factorial del numero ingresado es", factorial(num))
			except ValueError:
				print("Ingreso un simbolo incorrecto, vuelva a intentarlo desde el menu principal!")
		elif(opcion == 2):
			try:
				print("Ingrese la base de la potencia que desee calcular:")
				base = int(input())
				print("Ingrese el exponente de la potencia a calcular:")
				exp = int(input())
				print(base, "elevado al exponente", exp, "es igual a", potencia(base, exp))
			except ValueError:
				print("Ingreso un simbolo incorrecto, vuelva a intentarlo desde el menu principal!")
		elif(opcion == 3):
			try:
				print("Ingrese un numero entero para calcular la sucesion de Fibonacci:")
				num = int(input())
				print("La sucesion de Fibonacci para el termino numero", num, "es igual a", fibonacci(num))
			except ValueError:
				print("Ingreso un simbolo incorrecto, vuelva a intentarlo desde el menu principal!")
		elif(opcion == 0):
			print("Gracias por utilizar la calculadora especializada!")
			loop = False
		else:
			print("Ingreso una opcion incorrecta, vuelva a intentarlo!")