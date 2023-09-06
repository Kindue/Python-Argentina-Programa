# Ejercicio 7
# Dado el siguiente programa se pide:
# 1. Diga si el programa usa propiedades.
# 2. Qué hace el programa?


class Powers :
    def __init__ (self, square, cube ):
        self._square = square # _square is the base value
        self._cube = cube # square is the property name
    def getSquare(self):
        return self._square ** 2
    def setSquare(self, value):
        self._square = value
    square = property(getSquare, setSquare)
    def getCube(self):
        return self._cube ** 3
    cube = property ( getCube )


X = Powers (3, 4)
print (X.square) # 3 ** 2 = 9
print (X.cube) # 4 ** 3 = 64
X.square = 5
print (X.square) # 5 ** 2 = 25


#Utilizando propiedades, el programa calcula 3 al cuadrado, luego 4 al cubo y luego 5 al cuadrado