#Ejercicio 8
#Se puede incorporar a un conjunto los elementos de una lista
#sin utilizar iteraciones?


print("Puedo utilizar el metodo 'update' de los conjuntos para agregar los elementos de una lista a un conjunto")

lista = ["Javier", "Hernan", "Julian", "Mirta", "Susana", "Cristian"]

print("A modo de ejemplo esta es mi lista", lista)
print("Y quiero pasar los elementos a un conjunto sin utilizar iteraciones")

A = set()
print("Con mi conjunto A creado puedo usar 'A.update(lista)' y se 'actualizaran' los elementos que no estaban en A pero si en la lista")
A.update(lista)
print("Este es mi conjunto luego de utilizar 'update'", A)