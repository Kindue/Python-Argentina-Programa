#Ejercicio 9
#Defina un diccionario y muestre:
#1. Cómo se accede a un elemento de un diccionario
#2. Qué sucede si se intenta acceder al diccionario con una clave in-
#existente.
#3. ¿Cómo se calcula la longitud de un diccionario?

d = {52:"Patricio", 67:"Micaela", 24:"Gabriel", 98:"Julian"}
print("Este es el diccionario formado:", d)
print()
print("Puedo acceder a un elemento de manera directa si se la clave escribiendo 'd[52]', esto me devolvera:",d[52])
print("O puedo utilizar los metodos 'd.get(clave)', que me devolveran el valor asociado a la clave que pase por parametro:", d.get(52))
print()

print("Dependiendo de como quize acceder a una entrada inexistente voy a recibir un error o no:")
print("Si utilizo el metodo 'get' puedo hacer que este me devuelva un valor que yo le pase por parametro")
print("si es que no encuentra la clave en el diccionario. Si utilizo el get con una clave que no existe y un mensaje de error obtengo:")
print(d.get(53, "No encontre clave."), "Que fue mi mensaje de error")
print("Si intento acceder de manera directa a una clave que no existe voy a recibir un error de tipo KeyError")
print()

print("La longitud de un diccionario se calcula al igual que las listas y tuplas con el metodo 'len()'")
print("Al hacer 'len(d)' recibo la cantidad de entradas del diccionario:", len(d))