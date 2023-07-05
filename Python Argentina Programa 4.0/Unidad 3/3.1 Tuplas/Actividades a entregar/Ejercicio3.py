#Ejercicio 3
#Escriba un ejemplo que muestre que las tuplas son inmutables.


t = ('Carlos', 42, 0.3)
print("Mi tupla original:", t)
print("Con tuplas el operador '=' crea una nueva referencia y no refiere al objeto de la derecha del operador")
print("Probemos creando una nueva tupla r con los valores de t y agregandole un elemento a esa asignacion")

r = t
r += (5,)

print("Mi tupla t al agregar un elemento:", t)
print("Mi tupla r al agregar un elemento:", r)
print()

print("Si r y t fuesen listas las dos hubiesen cambiado, en cambio las tuplas son inmutables")