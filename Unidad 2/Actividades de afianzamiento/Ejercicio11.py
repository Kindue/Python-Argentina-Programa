#Ejercicio 11
#Escriba un programa que permita ingresar por teclado el nom-
#bre de una persona, la cantidad de horas trabajadas y luego el costo de
#la hora. El programa debe informar cuánto debe cobrar la persona.

print("Ingrese los siguientes datos para calcular cuanto deberia cobrar")

nombre = input("Ingrese su nombre: ")
horas = int(input("Ingrese la cantidad de horas trabajadas: "))
costo_por_hora = float(input("Ingrese el costo de su hora de trabajo: "))

monto_a_cobrar = (costo_por_hora * horas)

print(nombre + " debe cobrar ", monto_a_cobrar)