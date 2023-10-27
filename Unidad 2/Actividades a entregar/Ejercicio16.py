#Ejercicio 16
#Una juguetería tiene mucho éxito en dos de sus productos:
#payasos y muñecas. Suele hacer venta por correo y la empresa de lo-
#gística les cobra por el peso de cada paquete así que deben calcular el
#peso de los payasos y muñecas que saldrán en cada paquete a demanda.
#Cada payaso pesa 112 g y cada muñeca 75 g. Escriba un programa que
#lea el número de payasos y muñecas vendidos en el último pedido y
#calcule el peso total del paquete que será enviado.



print("Calculador de peso total del siguiente paquete")

print("Ingrese cantidad de payasos a enviar:")
cant_payasos = int(input())

print("Ingrese cantidad de muñecas a enviar")
cant_muñecas = int(input())

peso_total = (cant_payasos * 112) + (cant_muñecas * 75)

print("El peso total del siguiente envio sera de:", (peso_total) / 100, "kilogramos")
