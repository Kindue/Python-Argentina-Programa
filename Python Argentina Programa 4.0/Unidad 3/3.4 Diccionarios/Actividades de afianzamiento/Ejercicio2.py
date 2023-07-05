#Ejercicio 2
#Dado el siguiente diccionario d={1:"Daniel", 2:"Germán", 3:"
#Analía", 4:"José", 5:"Gabriel"} se pide:
#1. Devuelva el valor asociado a la clave 3.
#2. Calcule la longitud del diccionario.
#3. Devuelva las claves del diccionario.
#4. Devuelva los valores del diccionario.

d = {1:"Daniel", 2:"Germán", 3:"Analía", 4:"José", 5:"Gabriel"}
clave_tres = d[3]
longitud = len(d)
claves = d.keys()
valores = d.values()

print("La clave 3 tiene el siguiente elemento:", clave_tres)
print("La longitud del diccionario es:", longitud)
print("Las claves del diccionario son las siguientes:")
for c in (claves):
	print(c)
print("Los valores del diccionario son los siguientes:")
for v in valores:
	print(v)