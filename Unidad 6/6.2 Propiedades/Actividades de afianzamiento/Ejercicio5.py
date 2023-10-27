# Ejercicio 5
# Defina la clase Password la cual tiene un atributo de solo es-
# critura privado. Cuando un usuario desea leer el atributo se devuelve
# un error de lectura.


class Password:
    def __init__(self, clave):
        self._clave = clave

    def getClave(self):
        raise AttributeError("La clave es solo de escritura!")
    
    def setClave(self, nueva):
        self._clave = nueva

    clave = property(fget = getClave, fset = setClave)

print("Ingrese una clave:")
key = input()

nuevoPass = Password(key)
print("Ingrese una clave:")
key = input()
nuevoPass.clave = key
input()
try:
    nuevoPass.getClave()
except AttributeError:
    print("Error, no se puede revelar esta clave, no seas cochino")