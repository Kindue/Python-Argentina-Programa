#Ejercicio 3
#Escriba un programa que muestre las siguientes opciones:
#1. Calcular el perímetro de un triángulo.
#2. Calcular el área de un triángulo.
#Luego dependiendo de la opción elegida por el usuario calcule el área
#o perímetro de un triángulo cuyos datos son también ingresados por el
#usuario.


opcion = input("Ingrese 1 si desea calcular el perimetro de un triangulo o ingrese 2 si desea calcular el area de un triangulo: ")

if(opcion == '1'):
	lado1 = float(input("Ingrese un lado del triangulo: "))
	lado2 = float(input("Ingrese otro lado del triangulo: "))
	lado3 = float(input("Ingrese el lado restante del triangulo: "))
	perimetro = lado1 + lado2 + lado3
	print("El perimetro del triangulo ingresado es:", perimetro)
elif(opcion == '2'):
	base = float(input("Ingrese la base del triangulo: "))
	altura = float(input("Ingrese la altura del triangulo: "))
	area = (base * altura) / 2
	print("El area del triangulo ingresado es:", area)
else:
	print("No se ingreso una opcion valida!")