#Ejercicio 13
#Escriba un programa que pida al usuario dos números m y
#n el programa debe imprimir por pantalla el cociente y el resto de la
#división de m por n. Para este ejercicio asuma que n no puede ser 0.


print("Ingrese dos numeros para realizar la division entre esos dos numeros y mostrar el resultado y el resto")

print("Ingrese el dividendo:")
m = int(input())

print("Ingrese el divisor:")
n = int(input())

resultado = m / n

resto = m % n

print("El resultado de la division entre los numeros ingresados es:", resultado)
print("El resto de la division es:", resto)