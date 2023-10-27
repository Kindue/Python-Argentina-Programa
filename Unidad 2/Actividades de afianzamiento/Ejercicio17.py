#Ejercicio 17
#Imagine que acaba de abrir una nueva cuenta de ahorros que
#ofrece el 4 % de interés al año. Estos ahorros debido a intereses, que no
#se cobran hasta finales de año, se añaden al balance final de su cuenta
#de ahorros. Escriba un programa que comience leyendo la cantidad de
#dinero depositada en la cuenta de ahorros, introducida por el usuario.
#Después el programa debe calcular y mostrar por pantalla la canti-
#dad de ahorros tras el primer, segundo y tercer años. Redondear cada
#cantidad a dos decimales.


caja_ahorros = float(input("Ingrese la cantidad a depositar en su cuenta de ahorro: "))

primer_año = caja_ahorros * 1.04
print("El primer año se finaliza con $", round(primer_año, 2), "en ahorros")

segundo_año = primer_año * 1.04
print("El segundo año se finaliza con $", round(segundo_año, 2), "en ahorros")

tercer_año = segundo_año * 1.04
print("El tercer año se finaliza con $", round(tercer_año, 2), "en ahorros")
