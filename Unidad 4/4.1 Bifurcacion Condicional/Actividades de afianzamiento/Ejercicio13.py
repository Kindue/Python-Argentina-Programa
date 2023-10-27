#Ejercicio 13
#Escriba un programa para una empresa que tiene salas de
#juegos para todas las edades y quiere calcular de forma automática
#el precio que debe cobrar a sus clientes por entrar. El programa debe
#preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
#Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y
#18 años debe pagar $5 y si es mayor de 18 años, $10.


loop = True
while(loop):
	edad = int(input("Ingrese su edad para calcular el valor de la entrada: "))
	valor = -1

	if((edad >= 0) and (edad < 4)):
		valor = 0
	elif((edad >= 4) and (edad <= 18)):
		valor = 5
	elif(edad > 18):
		valor = 10

	if(valor != -1):
		if(valor == 0):
			print("La entrada es gratis!")
		else:
			print("El valor de su entrada es de $", valor)
	else:
		print("Ingreso una edad no valida!")

	opcion = input("Ingrese 0 para salir o cualquier otra tecla para continuar: ")
	if(opcion == '0'):
		loop = False