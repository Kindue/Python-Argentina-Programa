#Ejercicio 9:
#Para tributar un determinado impuesto se debe ser mayor de
#16 años y tener unos ingresos iguales o superiores a $1000 mensuales.
#Escriba un programa que pregunte al usuario su edad y sus ingresos
#mensuales y muestre por pantalla si el usuario tiene que tributar o no.


loop = True
while(loop):
	edad = int(input("Ingrese su edad: "))
	ingresos = int(input("Coloque sus ingresos mensuales: "))

	if((edad > 16) & (ingresos >= 1000)):
		print("Usted debe tributar!")
	else:
		print("No debe tributar!")

	opcion = input("Ingrese 0 para salir o cualquier otra tecla para continuar: ")
	if(opcion == '0'):
		loop = False