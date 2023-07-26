#Ejercicio 8
#Escriba una función que, dado un número de DNI, retorne True
#si el número es válido y False si no lo es. Para que un número de DNI
#sea válido debe tener entre 7 y 8 dígitos en base 10. Luego escriba un
#programa que pruebe la función.



def validarDNI(dni):
	dni = str(dni)
	if(len(dni) >= 7) and (len(dni) <= 8):
		return True
	else:
		return False


loop = True
while (loop):
	try:
		print("Ingrese un DNI para comprobar si es valido o ingrese 0 para terminar el programa: ")
		dni = int(input())
		if(dni == 0):
			loop = False
			print("Gracias por utilizar el validador!")
		else:
			if(validarDNI(dni)):
				print("El dni es valido!")
			else:
				print("El dni no es valido!")
	except ValueError:
		print("Ingreso un simbolo no valido, por favor intentelo de nuevo!")
