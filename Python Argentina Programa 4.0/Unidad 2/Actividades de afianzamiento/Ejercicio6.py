#Ejercicio 6
#Escriba un programa que permita calcular el promedio de cinco
#números ingresados por el usuario.

print("Calculadora de promedio de 5 numeros")					#Si no casteo mi n1 sera un string y luego el programa me tira error
n1 = float(input(print("Ingrese el 1er numero:")))
print("Ingrese el 2do numero: ")
n2 = float(input())												#Tengo que castear todos los numeros para que la suma no sea una concatenacion
print("Ingrese el 3er numero: ")								#de caracteres
n3 = float(input())
print("Ingrese el 4to numero: ")
n4 = float(input())
print("Ingrese el 5to numero: ")
n5 = float(input())

suma = float (n1 + n2 + n3 + n4 + n5)
resultado = suma / 5

print("El promedio es: ")
print(resultado)




#Solucion alternativa


#import sys

#n1= sys.argv[1] 					// Si lo hago asi recibe un string y el programa no funciona ya que trata de sumar strings
#n2= float sys.argv[2]				// Si lo hago asi casteo a un float el string que recibo
#n3= float sys.argv[3]
#n4= float sys.argv[4]
#n5= float sys.argv[5]

#suma = n1 + n2 + n3 + n4 + n5
#resultado = suma / 5

#print("El promedio es: ")
#print(resultado)
