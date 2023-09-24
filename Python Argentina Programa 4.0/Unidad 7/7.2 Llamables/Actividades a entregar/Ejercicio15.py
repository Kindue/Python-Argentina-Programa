# Ejercicio 15: Defina una función lambda que reciba como parámetro dos
# números enteros y retorne como resultado el mayor o, en caso de igual-
# dad, el primer argumento.



mayorOIgual = lambda x,y: x if(x >= y) else y

print(mayorOIgual(10, 5))
print(mayorOIgual(15, 20))
print(mayorOIgual(13, 13))