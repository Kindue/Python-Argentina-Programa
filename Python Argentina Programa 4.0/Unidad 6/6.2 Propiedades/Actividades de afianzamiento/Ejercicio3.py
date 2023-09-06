# Ejercicio 3
# Defina la clase semáforo la cual tiene tres variables: rojo, verde,
# amarillo. La clase simula el comportamiento de un semáforo de la vida
# real. Para resolver este ejercicio utilice propiedades.


class Semaforo:
    def __init__(self):
        self._rojo = False
        self._verde = False
        self._amarillo = False
    
    @property
    def rojo(self):
        return self._rojo
    
    @property
    def verde(self):
        return self._verde
    
    @property
    def amarillo(self):
        return self._amarillo
    
    def encenderRojo(self):
        self._rojo = True
        self._verde = False
        self._amarillo = False
    
    def encenderVerde(self):
        self._rojo = False
        self._verde = True
        self._amarillo = False
    
    def encenderAmarillo(self):
        self._rojo = False
        self._verde = False
        self._amarillo = True
    
    def apagar(self):
        self._rojo = False
        self._verde = False
        self._amarillo = False