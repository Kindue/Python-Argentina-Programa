# Ejercicio 4
# Muestre diferentes formas de violar la encapsulación del tipo
# de dato abstracto Persona.


import Ejercicio2

carlos = Ejercicio2.crearPersona('Carlos', 24)

print(carlos[0])

carlos[0] = 'Fernando'

print(carlos[1])

carlos[1] = 69

carlos.append('Marcos')

print(carlos)

#Ahora Carlos se llama Fernando que tiene 69 años y ademas 