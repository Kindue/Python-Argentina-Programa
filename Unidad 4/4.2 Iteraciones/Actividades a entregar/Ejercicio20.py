#Ejercicio 20
#Represente los datos de una persona con un diccionario. Los
#datos requeridos por personas son: dni, nombre, edad, domicilio, traba-
#jos. Por cada dato de una persona elija el tipo de dato más apropiado
#con excepción de los trabajos dado que una persona puede tener más
#de un trabajo entonces los mismos se representan con una tupla. Lue-
#go cree una lista de personas las cuales son ingresadas por el usuario.
#Posteriormente pida al usuario un número de dni e imprima los datos
#correspondiente a la persona que tenga el dni ingresado por el usuario.



listaPersonas = []
n = int(input("Ingrese la cantidad de personas que desea agregar: "))

for i in range(n):
	print("Ingrese los datos de una nueva persona!")
	dni = int(input("Ingrese el dni de la persona: "))
	nombre = input("Ingrese el nombre de la persona: ")
	edad = int(input("Ingrese la edad de la persona: "))
	domicilio = input("Ingrese el domicilio de la persona: ")
	cantTrabajos = int(input("Ingrese la cantidad de trabajos de la persona: "))
	trabajos = []
	for j in range(cantTrabajos):
		nuevoTrabajo = input("Ingrese un trabajo de la persona: ")
		trabajos.append(nuevoTrabajo)
	persona = {"dni": dni, "nombre": nombre, "edad": edad, "domicilio": domicilio, "trabajos": tuple(trabajos)}
	listaPersonas.append(persona)

print()
print("Busquemos una persona con su dni!")
documento = int(input("Ingrese el documento de la persona que desee conocer sus datos: "))

encontre = False

for p in listaPersonas:
	if(p['dni'] == documento):
		encontre = True
		print("El nombre de la persona con DNI", p['dni'], "es", p['nombre'])
		print("Su edad es", p['edad'])
		print("Su domicilio es", p['domicilio'])
		print("Sus trabajos son", p['trabajos'])

if(not(encontre)):
	print("El dni ingresado no esta en el lista de personas!")
