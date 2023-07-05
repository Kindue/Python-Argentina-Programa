#Ejercicio 3
#Realice las siguientes actividades en caso de que sea posible:
#1. Pase un conjunto a un diccionario.
#2. Pase un conjunto a un conjunto congelado.
#3. Pase un conjunto a una lista.
#4. Ordene un conjunto.
#5. Pase un conjunto a una tupla.

conjunto = {2, 4, 6, 8, 10, 12, 14, 16, 20}

#1- Los diccionarios necesitan una clave y un valor por lo tanto no son compatibles con los conjuntos que
# 	solamente necesitan un elemento por lo tanto no puedo pasar un conjunto a un diccionario.
#	Si intento hacer algo como la sentencia 'diccionario = dict(s)' voy a tener un error.

#2-

conjunto_congelado = frozenset(conjunto)
print(conjunto_congelado)

#3-

lista = list(conjunto)
print(lista)

#4- Los conjuntos son estructuras secuenciales desordenadas y no hay metodo para ordenarlos

#5-

tupla = tuple(conjunto)
print(tupla)