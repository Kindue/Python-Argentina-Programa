#Ejercicio 1
#Dada la siguiente lista l=[10,"hola",2.5,20,"que",3.5,30,"tal",4.5]
#se pide recuperar:
#1. el 30
#2. "hola"
#3. 10,"hola",2.5
#4. Los strings
#5. Los flotantes
#6. Los enteros

print("Primero mostremos la lista:")
lista=[10,"hola",2.5,20,"que",3.5,30,"tal",4.5]
print(lista)
	
el_30 = lista[6]
print("Ahora se guardo el 30, mire:")
print(el_30)

hola = lista[1]
print("Ahora se guardo el 'hola', mire:")
print(hola)

tres_elementos = lista[:3]
print("Ahora se guardo el 10, el 'hola' y el 2.5, mire:")
print(tres_elementos)

strings = lista[1::3]
print("Ahora se guardaron los strings en una lista diferente, mire:")
print(strings)

flotantes = lista[2::3]
print("Ahora se guardaron los flotantes en una lista diferente, mire:")
print(flotantes)

enteros = lista[::3]
print("Ahora se guardaron los enteros en una lista diferente, mire:")
print(enteros)
