#Ejercicio 5
#Implemente una calculadora de cuatro funciones. Para llevar
#adelante esta tarea ud debe:
#1. Definir una función suma.
#2. Definir una función resta.
#3. Definir una función multiplicación.
#4. Definir una función división.
#El programa debe mostrar un menú de opciones que le de la posibilidad
#al usuario de elegir la operación deseada y ejecutarla. El programa debe
#finalizar cuando el usuario ingresa la opción -1. Si el usuario ingresa
#una opción no válida el programa debe informar la situación y volver
#a mostrar el menú de opciones.


def suma(x, y):
	return x + y

def resta(x, y):
	return x - y

def multiplicacion(x, y):
	return x * y

def division(x, y):
	return x / y

loop = True
while(loop):
	valido = True
	print("A continuacion, ingrese la opcion de la funcion que desea ejecutar")
	print()
	print("--"*40)
	print()
	print("1 : SUMA  |  2 : RESTA  |  3 : MULTIPLICACION  |  4 : DIVISION  |  -1 : SALIR")
	print()
	print("--"*40)
	print()

	opcion = input()
	print()
	print("--"*40)

	if(opcion == '-1'):
		loop = False
		print("Gracias por utilizar la calculadora!")
	elif(opcion == '1'):
		while(valido):
			try:
				print("Ingrese el primer numero de la suma:")
				num1 = float(input())
				print("Ingrese el segundo numero de la suma:")
				num2 = float(input())
				resultado = suma(num1, num2)
				print("El resultado de la suma es el siguiente:", resultado)
				valido = False
			except ValueError:
				print("Uno de los numeros ingresados no es valido, por favor vuelva a intentarlo!")
	elif(opcion == '2'):
		while(valido):
			try:
				print("Ingrese el primer numero de la resta:")
				num1 = float(input())
				print("Ingrese el segundo numero de la resta")
				num2 = float(input())
				resultado = resta(num1, num2)
				print("El resultado de la resta es el siguiente:", resultado)
				valido = False
			except:
				print("Uno de los numeros ingresados no es valido, por favor vuelva a intentarlo!")
	elif(opcion == '3'):
		while(valido):
			try:
				print("Ingrese el multiplicando:")
				num1 = float(input())
				print("Ingrese el multiplicador:")
				num2 = float(input())
				resultado = multiplicacion(num1, num2)
				print("El resultado de la multiplicacion es el siguiente:", resultado)
				valido = False
			except:
				print("Uno de los numeros ingresados no es valido, por favor vuelva a intentarlo!")
	elif(opcion == '4'):
		while(valido):
			try:
				print("Ingrese el dividendo")
				num1 = float(input())
				print("Ingrese el divisor")
				num2 = float(input())
				resultado = division(num1, num2)
				print("El resultado de la division es el siguiente:", resultado)
				valido = False
			except:
				print("Uno de los numeros ingresados no es valido, por favor vuelva a intentarlo!")
	else:
		print("Opcion no valida vuelva a intentarlo!")
	print()
	print("--"*40)
