#Ejercicio 10
#Escriba un programa que permita que el usuario ingrese dos
#strings s0 y s1. El programa debe crear un nuevo string denominado
#merge el cual se forma a partir de s0 y s1 de la siguiente manera: primer
#carácter de s0, primer carácter de s1, segundo carácter de s0, segundo
#carácter de s1 y así siguiendo. Finalmente, el programa imprime s0, s1
#y r.


s0 = input("Ingrese el primer string: ")
s1 = input("Ingrese el segundo string: ")

i = 0
j = 0
mezcla = ''
while(i < len(s0) and j < len(s1)):
	mezcla += s0[i] + s1[j]
	i += 1
	j += 1

if(len(s0) > len(s1)):
	mezcla += s0[i:]
else:
	mezcla += s1[j:]


print("Este es el primer string ingresado:", s0)
print("Este es el segundo string ingresado:", s1)
print()
print("Esta es la mezcla entre los dos strings:", mezcla)