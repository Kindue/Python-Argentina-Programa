# Ejercicio 29: Defina la clase ContadorMódulo la cual implementa un con-
# tador módulo un número establecido por el usuario. Ejemplo:
# c=ContadorModulo (3)
# i=iter ( c )
# i . next () # 0
# i . next () # 1
# i . next () # 2
# i . next () # 0


class ContadorModulo:
    def __init__(self, modulo):
        self.modulo = modulo
        self.valor = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if(self.valor < self.modulo):
            resultado = self.valor
            self.valor += 1
            return resultado
        else:
            self.valor = 0
            return 0
        

c = ContadorModulo(3)
i = iter(c)
print(next(i))
print(next(i))
print(next(i))
print(next(i))