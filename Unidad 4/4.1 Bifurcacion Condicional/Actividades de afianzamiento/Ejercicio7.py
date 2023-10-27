#Ejercicio 7:
#Escriba un programa que pregunte al usuario su edad y muestre
#por pantalla si es mayor de edad o no. El programa también le debe
#solicitar al usuario la edad a partir de la cual se considera una persona
#mayor de edad.



loop = True
while(loop):
	mayor_de_edad = int(input("Ingrese la edad con la cual se considera que una persona es mayor de edad: "))
	edad = int(input("Ingrese su edad: "))
	if(edad >= mayor_de_edad):
		print("Usted es mayor de edad! No beba mientras conduce!")
	else:
		print("Usted no es mayor de edad! Tiene prohibida la compra de alcohol!")

	opcion = input("Ingrese 0 para salir o cualquier otra tecla para continuar: ")
	if(opcion == '0'):
		loop = False