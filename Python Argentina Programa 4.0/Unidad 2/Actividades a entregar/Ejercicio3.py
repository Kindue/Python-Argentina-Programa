#Ejercicio 3
#Escriba un programa que permita que el usuario ingrese dos
#números e imprima por pantalla la suma, resta y multiplicación de
#dichos número

print("Ingrese dos numeros para realizar la suma, la resta y la multiplicacion entre esos dos numeros")

num_uno = int(input("Ingrese el primer numero: "))														#lo mismo que print("")
num_dos = int(input("Ingrese el segundo numero: "))														#var = tipo_de_dato(input())

suma = num_uno + num_dos
resta = num_uno - num_dos
multiplicacion = num_uno * num_dos

print(f"La suma entre los numeros ingresados es igual a {suma} ")                                      	#Si agrego f al comienzo de lo
print("La resta entre los numeros ingresados es igual a", resta)										#que quiero mostrar e incluyo
print("La multiplicacion entre los dos numeros ingresados es igual a", multiplicacion)					#la variable dentro de {} puedo
																										#mostrarlo sin problema