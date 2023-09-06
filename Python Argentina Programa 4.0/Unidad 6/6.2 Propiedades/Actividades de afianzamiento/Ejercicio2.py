# Ejercicio 2
# Defina la clase Botón que permite almacenar el estado (Presio-
# nado, Libre) de un botón. Resuelva este ejercicio utilizando propieda-
# des.


class Boton:
    def __init__(self):
        self._estado = "Libre"
    
    @property
    def estado(self):
        return self._estado
    
    def presionar(self):
        if self._estado == "Libre":
            self._estado = "Presionado"
        else:
            self._estado = "Libre"


nuevoBoton = Boton()
nuevoBoton.presionar()
print(nuevoBoton.estado)
nuevoBoton.presionar()
print(nuevoBoton.estado)
nuevoBoton.presionar()
print(nuevoBoton.estado)