# Ejercicio 5: Escriba un programa que permita eliminar de una lista de nú-
# meros enteros positivos los números pares.

print("Ingrese cuantos numeros quiere ingresar:")
n = int(input())
numeros = []
for i in range(n):
    print("Ingrese un numero:")
    num = int(input())
    numeros.append(num)

numerosImpares = [x for x in numeros if x % 2 != 0]
print(numerosImpares)