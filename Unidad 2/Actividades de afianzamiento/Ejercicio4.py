#Ejercicio 4
#Escriba un programa que permita calcular el área y perímetro
#de un triángulo

print("Ingrese las medidas de los lados del triangulo y su altura")

base = float(input("Ingrese la medida de la base del triangulo: "))
hipotenusa = float(input("Ingrese la medida de la hipotenusa: "))
tercer_lado = float(input("Ingrese la medida del lado restante: "))
altura = float(input("Ingrese la altura del triangulo: "))

area_triangulo = (base * altura) / 2
perimetro_triangulo = base + hipotenusa + tercer_lado

print("El area del triangulo es: ", area_triangulo)
print("El perimetro del triangulo es: ", perimetro_triangulo)