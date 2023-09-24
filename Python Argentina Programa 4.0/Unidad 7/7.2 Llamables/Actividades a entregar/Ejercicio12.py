# Ejercicio 12: Defina la función remove-if la cual recibe como parámetro
# un predicado p y una lista l y retorna como resultado una lista que
# contiene los elementos de l excepto aquellos elementos para los cuales
# el predicado p es verdadero.


def removeif(p, l):
    if(l == []):
        return l
    elif(p(l[0])):
        return removeif(p, l[1:-1])
    else:
        return [l[0]] + removeif(p, l[1:-1])
    

par = lambda x : x % 2 == 0

print(removeif(par, [2,4,5,7,6,3,9]))