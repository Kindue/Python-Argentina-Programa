#Ejercicio 13
#Realice las siguientes actividades:
# 1. Explique el concepto de rodaja.
# 2. Explique el concepto de zancada.
# 3. Por cada concepto explicado de ejemplos.


#1- El concepto de rodaja se refiere a cortar una lista dada y rescatar sublistas de la lista original
#   utilizando las posiciones de la lista y especificando desde que posicion empieza la 'rodaja' y donde
#   termina

#2- Una zancada o stride consiste en recorrer una lista de a una cierta cantidad de pasos. Usualmente
#   las listas son recorridas de a un solo paso pero se puede especificar y cambiar para recorrer la
#   lista mas rapido y saltear elementos


lista = ["Carlos", 23, 0.4, "Leonardo", 48, 0.6, "Valentin", 65, 0.8]

print("Conociendo la siguiente lista", lista, "puedo operar con slices y strides")
print()

print("Si quiero recuperar solamente el primer grupo de String, Entero y Flotante utilizo 'lista[:3]'")
print("Es decir inicio desde la posicion 0 (lo omito ya que siempre se arranca del 0)")
print("Y termino en la posicion 3 sin tomar el elemento que esta en la posicion 3")
print()
print(lista[:3])
print()


print("Si quiero recuperar solamente los Strings de la lista utilizo 'lista[::3]'")
print("Es decir recorro la lista de principio a fin pero saltando 3 posiciones")
print()
print(lista[::3])
