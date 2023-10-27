#Ejercicio 6
#Dado el siguiente programa:
#def coordenadaZ ( x , y ) :
#x=x+10
#y=y+15
#return x+y
##programa principal
#x=int(input("Coordenada eje x: "))
#y=int(input("Coordenada eje y: "))
#for i in range (3) :
#z=coordenadaZ (x, y)
#x=x+1
#y=y+1
#print ( x , "␣ . ␣" , y , "␣ . ␣" , z )
#Se pide:
#1. De un ejemplo de ejecución del programa.
#2. Diga que hace el programa.


def coordenadaZ(x, y):
	x = x + 10
	y = y + 15
	return x + y

#programa principal
x = int(input("Coordenada eje x: "))
y = int(input("Coordenada eje y: "))
for i in range(3):
	z = coordenadaZ(x, y)
	x = x + 1
	y = y + 1
	print(x, "  .  ", y, "  .  ", z)


#Ejemplo de ejecucion con x = 5 e y = 7:
#
#Coordenada eje x: 5
#Coordenada eje y: 7
#6   .   8   .   37
#7   .   9   .   39
#8   .   10   .   41


#El programa utiliza la funcion coordenadaZ para crear una variable z segun los valores de x e y
#ingresados en el programa principal. La salida muestra como progresan las variables x, z e y
#a lo largo de 3 iteraciones. Cabe resaltar que las variables x e y solamente cambian con las asignaciones
#en el programa principal. Las variables x e y de la funcion son variables locales de la funcion
#y no cambian a las variables globales del programa principal.