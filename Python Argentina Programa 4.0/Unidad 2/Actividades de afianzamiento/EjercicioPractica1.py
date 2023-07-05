#Ejercicio zoom
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
#dd/mm/aaaa y muestre por pantalla, el dia, el mes y el año
#Adaptar el programa anterior para que tambien funcione cuando el dia o el mes
#se introduzcan con un solo caracter


fecha = input("Ingrese la fecha de nacimiento en formato dd/mm/aaaa: ")

fecha = fecha.split("/")

dia = fecha[0]
mes = fecha[1]
anio = fecha[2]

print("Su fecha de nacimiento es el dia",dia,"del mes",mes,"del año",anio)