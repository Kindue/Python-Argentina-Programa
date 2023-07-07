#Ejercicio 10
#Los alumnos de un curso se han dividido en dos grupos A y
#B de acuerdo al sexo y el nombre. El grupo A esta formado por las
#mujeres con un nombre anterior a la M y los hombres con un nombre
#posterior a la N y el grupo B por el resto. Escriba un programa que
#pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
#que le corresponde.


loop = True
while(loop):
	nombre = input("Ingrese su nombre: ")
	sexo = input("Ingrese su genero, femenino o masculino: ")

	if((nombre[0].upper() in 'A'...'L') and (sexo.upper() == 'FEMENINO')) or ((nombre[0].upper() in 'O'...'Z') and (sexo.upper() == 'MASCULINO')):
		print("Usted pertenece al Grupo A!")
	else:
		print("Usted pertenece al Grupo B!")


	opcion = input("Ingrese 0 para salir o cualquier otra tecla para continuar: ")
	if(opcion == '0'):
		loop = False
