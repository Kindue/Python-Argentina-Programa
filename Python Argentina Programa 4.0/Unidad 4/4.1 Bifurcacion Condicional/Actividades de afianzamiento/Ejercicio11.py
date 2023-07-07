#Ejercicio 11
#Los tramos impositivos para la declaración de la renta en un
#determinado país son mostrados en la tabla 1.
#
#		Renta						Tipo Impositivo
#
#		Menos de $10000				5%
#		Entre $10000 y $20000		15%
#		Entre $20000 y $35000		20%
#		Entre $35000 y $60000		30%
#		Más de $60000				45%
#
#
#Escriba un programa que pregunte al usuario su renta anual y muestre
#por pantalla el tipo impositivo que le corresponde.


loop = True
while(loop):
	renta = int(input("Ingrese su renta anual para conocer el tipo impositivo que le corresponde: "))
	impositivo = 0

	if((renta > 0) and (renta < 10000)):
		impositivo = 5
	elif((renta >= 10000) and (renta < 20000)):
		impositivo = 15
	elif((renta >= 20000) and (renta < 35000)):
		impositivo = 20
	elif((renta >= 35000) and (renta < 60000)):
		impositivo = 30
	elif(renta >= 60000):
		impositivo = 45

	print("Segun su renta usted le corresponde un impuesto del", impositivo, "%")

	opcion = input("Ingrese 0 para salir o cualquier otra tecla para continuar: ")
	if(opcion == '0'):
		loop = False