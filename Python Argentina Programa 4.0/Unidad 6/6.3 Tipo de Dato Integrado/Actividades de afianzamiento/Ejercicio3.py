# Ejercicio 3: Defina el tipo de dato ContadorLimitado el cual permite al-
# macenar un valor inicial y un valor límite. Un contador limitado va
# incrementando su valor hasta que llega al límite. Si el contador está en
# el límite y se le da la orden de contar se mantiene en el valor límite. El
# tipo debe permitir:
# 1. Crear un contador con un valor límite. Si un contador se crea sin
# un valor límite se produce una excepción TypeError.
# 2. Crear un contador con un valor inicial y un valor límite. Si un
# contador se crea sin un valor límite se produce una excepción
# TypeError.
# 3. Proveer una representación textual de un contador.
# 4. Convertir a un string un contador.
# 5. Comparar estudiantes utilizando los operadores relacionales ==,<,<=,>,>=.
# 6. Convertir un contador a int, float, str.
# 7. Asignar un contador a otro contador utilizando la asignación =.


class ContadorLimitado:
    def __init__(self, vLim=0, vIni=0):
        if(vLim != 0):
            self.vActual = vIni
            self.vLimite = vLim
        else:
            raise TypeError("Valor limite no valido, intente de nuevo")
        
    def __repr__(self):
        return (f"ContadorLimitado({self.vActual}, {self.vLimite})")
    
    def __str__(self):
        return repr(self)
    
    