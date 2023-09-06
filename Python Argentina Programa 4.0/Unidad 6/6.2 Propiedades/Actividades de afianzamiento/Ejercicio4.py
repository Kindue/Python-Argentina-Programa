# Ejercicio 4
# Defina la clase SemaforoConBotón la cual tiene un botón y un
# semáforo. El semáforo funciona de la siguiente manera: Se presiona el
# botón se enciende la luz roja, se presiona nuevamente se apaga la luz
# roja, cuando se presiona de nuevo se prende la luz verde, si se presiona
# nuevamente se apaga la luz verde, se presiona nuevamente se prende la
# luz amarilla y luego de otra presión se apaga la luz amarilla y comienza
# el ciclo nuevamente.

from Ejercicio2 import Boton
from Ejercicio3 import Semaforo

class SemaforoConBoton:
    def __init__(self):
        self._boton = Boton()
        self._semaforo = Semaforo()
    
    def presionarBoton(self):
        if self._boton.estado == "Presionado":
            if self._semaforo.rojo:
                self._semaforo.encenderVerde()
            elif self._semaforo.verde:
                self._semaforo.encenderAmarillo()
            elif self._semaforo.amarillo:
                self._semaforo.encenderRojo()
        self._boton.presionar()

    def getEstadoSemaforo(self):
        return {
            "rojo": self._semaforo.rojo,
            "verde": self._semaforo.verde,
            "amarillo": self._semaforo.amarillo
        }
    

semaforo_con_boton = SemaforoConBoton()
semaforo_con_boton.presionarBoton()
print(semaforo_con_boton.getEstadoSemaforo())
semaforo_con_boton.presionarBoton()
print(semaforo_con_boton.getEstadoSemaforo())