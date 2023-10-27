#Ejercicio 15
#Escribir un programa que pregunte al usuario una cantidad a
#invertir, el interés anual y el número de años, y muestre por pantalla el
#capital obtenido en la inversión.


print("Calculadora de inversiones a largo plazo")

print("Ingrese la cantidad inicial a invertir: ")
monto_a_invertir = float(input())

print("Ingrese el interes anual: ")
interes_anual = float(input())

print("Ingrese numero de años: ")
años = int(input())

capital_obtenido = (((monto_a_invertir / 100) * interes_anual) * años)

print("En", años, "años su ganancia sera de", capital_obtenido, "pesos")