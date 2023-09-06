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
        else:
            raise ValueError("El valor actual no puede superar al valor limite!")

    def __repr__(self):
        return (f"ContadorLimitado({self.vActual}, {self.vLimite})")
    
    def __str__(self):
        return repr(self)
   
try:
    print("Ingrese un valor inicial del contador:")
    vInicial = int(input())
    print("Ingrese el valor maximo del contador:")
    vMaximo = int(input())
except ValueError:
    print("Ingreso una entrada no valida!")

try:
    contador = ContadorLimitado(vMaximo, vInicial)
    for num in range(vMaximo):
        print(contador)
        contador.incrementarValor()

    contador.incrementarValor()
except ValueError:
    print("No puedo seguir aumentando el valor")