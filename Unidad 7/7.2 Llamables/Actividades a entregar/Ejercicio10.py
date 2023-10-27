# Ejercicio 10: Defina la función butlast la cual recibe como parámetro un
# entero n y una lista l y retorna la lista pero con los n últimos ítems
# eliminados.


def butlast(n, l):
    return l[0:len(l) - n]

print(butlast(4, [6,2,4,5,8]))