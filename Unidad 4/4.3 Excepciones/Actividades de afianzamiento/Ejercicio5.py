#Ejercicio 5
#Escriba un ejemplo que dispare una excepción, la controle y
#muestre el uso de finally.



tupla = {}
suma = 0
loop = True
while(loop):
	try:
		print("Ingrese un numero al conjunto o ingrese '0' para terminar:")
		num = int(input())
		if(num == 0):
			loop = False
		else:
			suma = suma + num
	except ValueError:
		print("Ingreso un valor no numerico, intentelo de nuevo!")
	finally:
		print("Valor de la suma de todos los elementos del conjunto:")
		print(suma)