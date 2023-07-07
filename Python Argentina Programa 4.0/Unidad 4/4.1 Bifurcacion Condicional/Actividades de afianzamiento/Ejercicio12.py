#Ejercicio 12
#En una determinada empresa, sus empleados son evaluados
#al final de cada año. Los puntos que pueden obtener en la evaluación
#comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores
#beneficios. Los puntos que pueden conseguir los empleados pueden ser
#0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencio-
#nadas. A continuación se muestra una tabla con los niveles correspon-
#dientes a cada puntuación. La cantidad de dinero conseguida en cada
#nivel es de $2.400 multiplicada por la puntuación del nivel.
#
#	Niveles				Puntuacion		
#	Inaceptable			0.0
#	Aceptable			0.4
#	Meritorio  			0.6 o mas
#
#Escriba un programa que lea la puntuación del usuario e indique su
#nivel de rendimiento, así como la cantidad de dinero que recibirá el
#usuario.



loop = True 
while(loop):
	puntuacion = float(input("Ingrese puntuacion para indicar su nivel y la cantidad de dinero que recibira: "))
	nivel = ''
	dinero = 2400 * puntuacion

	if(puntuacion == 0.0):
		nivel = 'Inaceptable'
	elif(puntuacion == 0.4):
		nivel = 'Aceptable'
	elif(puntuacion >= 0.6):
		nivel = 'Meritorio'

	if(nivel != ''):
		print("Su nivel de rendimiento es", nivel, "y el dinero que recibira por su empeño es de $", dinero)
	else:
		print("Se ha ingresado una puntuacion no valida")

	opcion = input("Ingrese 0 para salir o cualquier otra tecla para continuar: ")
	if(opcion == '0'):
		loop = False