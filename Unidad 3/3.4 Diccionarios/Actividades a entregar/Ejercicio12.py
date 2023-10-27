#Ejercicio 12
#Se pueden sacar rodajas en los diccionarios?


print("Los diccionarios no tienen un metodo para hacer rodajas de forma directa")

print("Pero podemos convertir los elementos de un diccionario a una lista para hacer las rodajas")
print("Y luego convertir estas rodajas a un diccionario")

d = {24:"Juan", 28:"Camila", 32:"Jose", 36:"Pablo" }
print()
print("A modo de ejemplo convertimos el diccionario d con los siguientes elementos a una lista de duplas")
print("Diccionario d:", d)

lista = []
for i in d.items():
	lista.append(i)
print("Lista de duplas del diccionario d", lista)

print("Si queremos hacer una rodaja con los primeros dos elementos cortamos la lista de elementos")
print("Lista con los dos primeros elementos del diccionario d", lista[0:2])

print("Utilizamos un diccionario auxiliar para no perder los demas elementos del diccionario")
d_aux = {}
for i in lista[0:2]:
	d_aux[i[0]] = i[1]

print("Este es mi diccionario con solamente sus primeros dos elementos:", d_aux)