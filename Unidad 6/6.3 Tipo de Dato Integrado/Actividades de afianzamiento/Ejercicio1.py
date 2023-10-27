# Ejercicio 1
# Defina la clase Punto la cual permite realizar las siguientes
# operaciones:
# 1. Crear un punto en el origen de coordenadas o en coordenadas
# indicadas por el usuario.
# 2. Sumar puntos utilizando el operador +.
# 3. Restar puntos utilizando el operador -.
# 4. Recuperar la coordenada x de un punto.
# 5. Convertir un punto en una tupla.
# 6. Comparar dos puntos utilizando el operador ==.
# 7. Convertir un punto a tupla, lista y string.
# 8. Proveer una representación textual de un punto.


class Punto:
    def __init__(self, coordX=0, coordY=0):
        self._x = coordX
        self._y = coordY

    def _getX(self):
        return self._x
    
    def _getY(self):
        return self._y
    
    def _setX(self, nuevo):
        self._x = nuevo

    def _setY(self, nuevo):
        self._y = nuevo
    
    x = property(fget = _getX, fset = _setX, fdel = None, doc = None)
    y = property(fget = _getY, fset = _setY, fdel = None, doc = None)

    def __add__(self, other):
        return Punto(self._x + other.x, self._y + other.y)
    
    def __sub__(self, other):
        return Punto(self._x - other.x, self._y - other.y)
    
    def convTupla(self):
        return (self._x, self._y)
    
    def __eq__(self, other):
        return (self._x == other.x and self._y == other.y)
    
    def __repr__(self):
        return (f"Punto:({self._x}, {self._y})")
    
    def __str__(self) -> str:
        return self.__repr__()

    

puntoA = Punto()
puntoB = Punto(12, 24)
puntoC = Punto(20, 10)

print(puntoA)
print(puntoB)
print(puntoC)

puntoN = puntoB + puntoC
puntoM = puntoB - puntoA

print(puntoN)
print(puntoM)

print(puntoM == puntoB)

tupla = puntoB.convTupla()

eval("puntoC")