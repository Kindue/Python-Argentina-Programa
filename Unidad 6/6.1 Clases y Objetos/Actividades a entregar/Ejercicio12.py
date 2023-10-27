# Ejercicio 12
# Defina la clase ContadorLimitado. Un contador limitado es
# un contador que puede contar hasta un límite establecido por el pro-
# gramador. La clase soporta las siguientes operaciones:
# 1. Inicializar el contador en algún valor menor o igual que el valor
# máximo admitido.
# 2. Retornar el valor actual del contador.
# 3. Incrementar el contador en uno.
# 4. Devolver una representación del contador admitida por eval().

class ContadorLimitado:
    def __init__(self, limite, inicial=0):
        if(inicial > limite):
            raise ValueError("El valor inicial no puede ser mayor al valor limite")
        self.vLimite = limite
        self.vActual = inicial

    def obtenerValor(self):
        return self.vActual
    
    def incrementarValor(self):
        if(self.vActual < self.vLimite):
            self.vActual += 1

    def __repr__(self):
        return f"ContadorLimitado({self.vActual}, {self.vLimite})"
