#Ejercicio 14
#Escriba un programa que permita realizar la conversión a dó-
#lares y euros de una cantidad de pesos ingresada por el usuario.


print("Ingrese la cantidad de pesos que desee conocer su valor en dolares y euros: ")
pesos = float(input())

dolar_por_peso_hoy = 0.0042

euro_por_peso_hoy = 0.0040

print(pesos, "equivalen a", pesos * dolar_por_peso_hoy, "dolares")
print(pesos, "equivalen a", pesos * euro_por_peso_hoy, "euros")