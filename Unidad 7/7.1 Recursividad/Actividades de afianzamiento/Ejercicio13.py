# Ejercicio 13: Defina función recursiva combinaciones(lista, k) la cual recibe
# como parámetro una lista de caracteres únicos, y un número k. La
# función retorna como resultado todas las posibles cadenas de longitud
# k formadas con los caracteres dados (se premiten caracteres repetidos).
# >>> combinaciones ( [ ’ a ’ , ’b ’ , ’ c ’ ] , 2)
# aa ab ac ba bb bc ca cb cc

def combinaciones(lista, k):
    if(k > 0):
        indice = len(lista) - 1
        return combinacionesAux(lista, k, indice)
    else:
        return []

def cadenas(listaARet, k, indiceActual, lista):
    if(len(l) == 0):
        listaARet.append(lista[indiceActual])
    else:
        listaARet.append(lista[indiceActual])

def combinacionesAux(lista, k, indice):
    if(indice == 0):
        aRet = 