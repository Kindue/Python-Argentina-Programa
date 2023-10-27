#Ejercicio 8
#Escriba un ejemplo que muestre que los diccionarios son mu-
#tables.


d = {1:"Juan", 2:"Jose", 3:"Maria", 4:"Martina"}

print("Este es mi diccionario original:", d)

#En los diccionarios los valores son mutables pero sus claves no lo son. En nuestro caso puedo cambiar los Strings
#Que son los valores del diccionario pero no los Enteros que son las claves

d[1] = "Nicolas"
d.setdefault(5, "Martin")

print("Cambio el valor asociado a la clave 1 que era 'Juan', ahora es 'Nicolas'")
print("Ademas agrego una nueva entrada con clave 5 y valor 'Martin'")
print("Este es mi diccionario luego de hacer los cambios:", d)

print("Por otro lado las claves no tienen forma de ser cambiadas, son elementos inmutables")