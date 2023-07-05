#Ejercicio Practica 1
#Escriba un programa en Python que solicita un string al usuario y genere un diccionario donde las claves son cada 
#caracter del string y los valores sean el número de veces que ese caracter aparece en el string.
#Posteriormente, deberá imprimir:
#a) el diccionario completo
#b) el caracter que aparece con más frecuencia en dicho string y su frecuencia. 
#Por ejemplo:
#string: "Hola habitantes de la tierra"
#{'H': 1, 'o': 1, 'l': 2, 'a': 5, ' ': 4, 'h': 1, 'b': 1, 'i': 2, 't': 3, 'n': 1, 'e': 3, 's': 1, 'd': 1, 'r': 2}
#Caracter con mayor frecuencia: a
#Cantidad de apariciones: 5


d = {}
mayores = []
sentencia = input("Ingrese el string para generar un diccionario: ")
for letra in sentencia:
	if(letra not in d):
		d[letra] = sentencia.count(letra)


mayor = 0
for valor in d.values():
	if(valor > mayor):
		mayor = valor


print("El string ingresado es el siguiente:", sentencia)
print()
print("El diccionario creado es el siguiente:")
print(d)
print()
