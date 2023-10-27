# Ejercicio 1
# Defina la clase Persona la cual permite almacenar el nombre y
# la edad de una persona. Resuelva este ejercicio utilizando propiedades.


class Persona:
    def __init__(self, nb, ed):
        self.nombre = nb
        self.edad = ed
    @property
    def getNombre(self):
        return self._nombre
    @property
    def getEdad(self):
        return self._edad
    @nombre.setter
    def setNombre(self, nuevo):
        self._nombre = nuevo
    @edad.setter
    def setEdad(self, nuevo):
        self._edad = nuevo

    def _del_nombre(self):
        del self._nombre

    def _del_edad(self):
        del self._edad

    def __str__(self):
        return f"Persona: {self._nombre} , {self._edad}"

    # nombre = property(fget = getNombre, fset = setNombre, fdel = _del_nombre, doc= "La propiedad nombre de Persona")
    # edad =  property(fget = getEdad, fset = setEdad, fdel = _del_edad, doc= "La propiedad edad de Persona")


carlos = Persona("Carlos", 56)
print(carlos.nombre)
print(carlos.edad)

carlos.nombre = "Carlitos"
carlos.edad = 60

print(carlos)