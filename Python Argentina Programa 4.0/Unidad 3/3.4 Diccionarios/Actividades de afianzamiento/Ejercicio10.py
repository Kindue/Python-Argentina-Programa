#Ejercicio 10
#Escriba un programa que permite que el usuario ingrese dos
#valores en las variables a y b y luego determinaa si dichos valores se
#encuentran almacenados como valor en el diccionario d. El diccionario
#d es ingresado por el usuario.


d = {}

n = int(input("Ingrese la cantidad de entradas en el diccionario a crear: "))
print("Ingrese las entradas del diccionario, primero ingresando la clave y luego su valor asociado:")

for i in range(n):
	clave = input("Ingrese una clave: ")
	valor = input("Ingrese su valor asociado: ")
	d[clave] = valor

a = input("Ingrese el primer elemento a buscar en el diccionario: ")
b = input("Ingrese el segundo elemento a buscar en el diccionario: ")

print()
if(a in d.values()):
	print(a, "esta en el diccionario")
else:
	print(a, "no esta en el diccionario")

print()

if(b in d.values()):
	print(b, "esta en el diccionario")
else:
	print(b, "no esta en el diccionario")