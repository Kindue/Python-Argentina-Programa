#Ejercicio 12
#Escriba un programa que calcule el IMC (índice de Masa Cor-
#poral).


print("Calculadora del indice de masa corporal")
print("Ingrese su altura en metros:")
altura = float(input())
print("Ingrese su peso en kilogramos:")
peso = float(input())

IMC = peso / (altura * altura)

print("Su IMC es:", IMC)