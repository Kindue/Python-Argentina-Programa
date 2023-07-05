#Ejercicio 8
#Cree una lista y muestre:
# 1. El acceso a un elemento de la lista.
# 2. Qué sucede si se intenta acceder a una posición inexistente de la
#lista.
# 3. Cómo se calcula la longitud de una lista.


lista = ["Carlos", 23, 0.42, "Javier", True, 420]

print("A modo de ejemplo, la lista fue creada con 6 elementos")
print("Esta es la lista", lista)
print("Mostremos el cuarto elemento que corresponde al indice 3 en nuestra lista:", lista[3])

print()

print("Podemos calcular el largo de la lista para confirmar que hay 6 elementos")
print("Al hacer 'len(lista)' podemos calcular cuantos elementos hay, en nuestro caso hay", len(lista), "elementos")

print()

print("Al haber",len(lista), "elementos tendremos los indices de 0 a", (len(lista) - 1))
print("Entonces si queremos acceder al elemento en la posicion 6, tendremos un error, mostrando que nos 'caimos' de la lista:")

print()

print(lista[6])

