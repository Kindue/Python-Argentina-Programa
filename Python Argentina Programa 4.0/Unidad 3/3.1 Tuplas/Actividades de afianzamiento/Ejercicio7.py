#Ejercicio 7
#Defina una tupla y muestre:
#1. Cómo se accede a un elemento de la tupla?
#2. Qué sucede si se intenta acceder a una posición inexistente de la
#tupla?
#3. Cómo se calcula la longitud de una tupla?


tupla = ("Sergio", 42, 0.23, "Carlos", True, 69)

print("A modo de ejemplo, la tupla fue creada con 6 elementos")
print("Esta es la tupla", tupla)
print("Mostremos el cuarto elemento que corresponde al indice 3 en nuestra tupla:", tupla[3])

print()

print("Podemos calcular el largo de la tupla para confirmar que hay 6 elementos")
print("Al hacer 'len(tupla)' podemos calcular cuantos elementos hay, en nuestro caso hay", len(tupla), "elementos")

print()

print("Al haber",len(tupla), "elementos tendremos los indices de 0 a", (len(tupla) - 1))
print("Entonces si queremos acceder al elemento en la posicion 6, tendremos un error, mostrando que nos 'caimos' de la tupla:")

print()

print(tupla[6])