#Ejercicio 5
#Escriba un programa que permita que el usuario ingrese dos
#valores numéricos. Luego el programa le pregunta al usuario si quiere
#sumar, restar dividir o multiplicar y dependiendo de la opción elegida
#el programa realiza la operación correspondiente.


k = float(input("Ingrese el primer numero: "))
h = float(input("Ingrese el segundo numero: "))

print("A continuacion ingrese la opcion correspondiente a la operacion que desee realizar entre los dos valores ingresados")
print("1 : Si desea sumar        2 : Si desea restar        3 : Si desea multiplicar        4 : Si desea dividir")
opcion = input()


if(opcion == '1'):
	print("El resultado de la suma entre los dos valores ingresados es:", k+h)
elif(opcion == '2'):
	print("El resultado de la resta entre los dos valores ingresados es:", k-h)
elif(opcion == '3'):
	print("El resultado de la multiplicacion entre los dos valores ingresados es:", k*h)
elif(opcion == '4'):
	print("El resultado de la division entre los dos valores ingresados es:", k/h)
else:
	print("La opcion ingresada no es valida!")