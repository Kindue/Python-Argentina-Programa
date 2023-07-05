#Ejercicio 4
#Escriba un programa que permita determinar si una ecuación
#de segundo grado tiene:
#1. Dos soluciones reales distintas. Una ecuación de segundo grado
#tiene dos soluciones si el discriminante b2 − 4ac es mayor que cero.
#2. Una única solución real. Una ecuación de segundo grado tiene dos
#soluciones si el discriminante b2 − 4ac es igual que cero.
#3. No tiene solución real. Una ecuación de segundo grado tiene dos
#soluciones si el discriminante b2 − 4ac es menor que cero.
#Nota: Todos los valores requeridos por la ecuación son ingresados por
#el usuario.


t_independiente = int(input("Ingrese el termino independiente de la ecuacion de segundo grado: "))
grado_uno = int(input("Ingrese el coeficiente de grado 1 de la ecuacion de segundo grado: "))
grado_dos = int(input("Ingrese el coeficiente de grado 2 de la ecuacion de segundo grado: "))

discriminante = (grado_uno * grado_uno) - (4 * grado_dos * t_independiente)

if(discriminante > 0):
	print("La ecuacion ingresada tiene dos soluciones reales!")
elif(discriminante < 0):
	print("La ecuacion ingresada no tiene soluciones reales!")
else:
	print("La ecuacion ingresada tiene solamente una solucion!")