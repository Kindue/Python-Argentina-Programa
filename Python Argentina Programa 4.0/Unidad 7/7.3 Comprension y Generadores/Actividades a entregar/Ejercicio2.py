# Ejercicio 2: Escriba una lista que permita generar una lista de potencias
# de dos.

print("Ingrese un numero:")
n = int(input())
potencias_de_dos = [2 ** i for i in range(n)]
print(potencias_de_dos)