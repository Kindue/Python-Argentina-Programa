#Ejercicio 13
#Se pueden hacer zancadas en los diccionarios?


print("Al igual que con las rodajas, los diccionarios no tienen un metodo para hacer zancadas de forma directa")

print("Pero podemos convertir los elementos de un diccionario en una lista de duplas para hacer las zancadas necesarias")
print("Y luego recuperar los elementos de la lista segun como queramos recorrer con zancadas")

d = {24:"Juan", 28:"Camila", 32:"Jose", 36:"Pablo", 40:"Beatriz", 44:"Hernan", 48:"Julian", 52: "Pedro", 56:"Susana", 60:"Alejandra" }
print()
print("A modo de ejemplo convertimos el diccionario d con los siguientes elementos a una lista de elementos")
print("Diccionario d:", d)

lista = []
for i in d.items():
	lista.append(i)
print("Lista de duplas del diccionario d", lista)

print("Si queremos recorrer el diccionario y recuperar un elemento cada tres que recorramos hacemos una zancada de tres pasos con la lista")
print("Lista con los elementos recuperados luego de hacer una zancada de tres pasos", lista[::3])

print("Utilizamos un diccionario auxiliar para no perder los demas elementos del diccionario")
d_aux = {}
for i in lista[::3]:
	d_aux[i[0]] = i[1]

print("Este es mi diccionario con los elementos recuperados tras la zancada", d_aux)