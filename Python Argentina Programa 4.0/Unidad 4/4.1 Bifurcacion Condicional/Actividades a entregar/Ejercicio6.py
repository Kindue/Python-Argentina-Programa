#Ejercicio 6
#Escriba un programa que permita que el usuario ingrese el
#nombre de dos equipos y la cantidad de goles que han hecho en un
#partido. Luego el programa imprime el nombre del equipo ganador y
#bien el nombre de los dos equipos en caso de empate.


loop = True
while (loop):
	equipo_uno = input("Ingrese el nombre del primer equipo: ")
	goles_e1 = int(input("Ingrese la cantidad de goles que convirtio el primer equipo: "))
	equipo_dos = input("Ingrese el nombre del segundo equipo: ")
	goles_e2 = int(input("Ingrese la cantidad de goles que convirtio el segundo equipo: "))

	if(goles_e1 > goles_e2):
		print(equipo_uno, "gano el partido", goles_e1, "a", goles_e2)
	elif(goles_e1 < goles_e2):
		print(equipo_dos, "gano el partido", goles_e2, "a", goles_e1)
	else:
		print(equipo_uno, "y", equipo_dos, "empataron", goles_e1, "a", goles_e2)

	opcion = input("Ingrese 0 para salir o cualquier otra tecla para continuar: ")
	if(opcion == '0'):
		loop = False