#Ejercicio 4:
#Escriba un ejemplo que muestre que las listas son mutables.

lista = [428, "JRR", 0.257009346]

print("Esta es mi lista original:",lista)

lista[0] = "Lionel Messi"

print("Ahora cambie su primer componente, esta es mi lista ahora:", lista)

lista[1] = 0.811428571

print("Ahora cambie el segundo componente, esta es mi lista ahora:", lista)

lista[2] = 875

print("Ahora cambie el tercer componente, esta es mi lista ahora:", lista)

print("Mutamos nuestra lista original por completo")