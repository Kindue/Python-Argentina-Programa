#Ejercicio 18
#Escriba un programa que permita ingresar una cantidad de
#dinero c y un porcentaje p. El programa debe calcular el porcentaje p
#de dinero de c.


print("Calculadora de porcentaje de cierto monto de dinero")

print("Ingrese un monto de dinero: ")
c = float(input())

print("Ingrese el porcentaje a utilizar: ")
p = float(input())

resultado = (c / 100) * p

print("El", p, "% de $", c, "es $", resultado)