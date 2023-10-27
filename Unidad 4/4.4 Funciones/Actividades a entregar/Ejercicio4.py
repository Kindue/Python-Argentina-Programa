#Ejercicio 4
#Realice las siguientes actividades:
#1. Defina la función invertir string la cual recibe como parámetro un
#string s y retorna como resultado otro string cuyo contenido es el
#de s pero en orden inverso.
#2. Defina la función invertirTodo la cual recibe como parámetro la
#lista l de strings y retorna como resultado la lista l con los strings
#invertidos.
#3. Construya un programa principal que:
#a) Permita que el usuario ingrese una lista de strings ls.
#b) Invierta los strings de ls.
#c) Imprima ls y ls invertida.


def invertir(s):
	return s[-1::-1]

def invertirTodo(lista):
	for i in range(len(lista)):
		l[i] = invertir(l[i])

l = []
loop = True
while (loop):
	try:
		n = int(input("Ingrese la cantidad de numeros que desea insertar en la lista: "))
		loop = False
		print("--"*40)
	except ValueError:
		print("Ingreso un simbolo no valido, por favor intentelo de nuevo")

for k in range(n):
	string = str(input("Ingrese un caracter para agregar a la lista: "))
	l.append(string)

print()
print("--"*40)
print()
print("Esta es la lista ingresada:")
print(l)
print("--"*40)
invertirTodo(l)
print("Esta es la lista ingresada con sus strings invertidos:")
print(l)
print("--"*40)
#l.reverse()
#print("Esta es la lista invertida con sus strings tambien invertidos")
#print(l)
#print("--"*40)

