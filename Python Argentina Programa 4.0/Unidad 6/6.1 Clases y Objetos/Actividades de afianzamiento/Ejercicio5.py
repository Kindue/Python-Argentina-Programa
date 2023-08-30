# Ejercicio 5
# Defina una clase con una variable de instancia privada. Luego
# muestre que la privacidad es llevada a cabo por convención.


class Rectangulo:
	def __init__(self, b, a):
		self._base = b
		self._altura = a

	def getBase(self):
		return self._base

	def getAltura(self):
		return self._altura

	def setBase(self, b):
		self._base = b

	def setAltura(self, a):
		self._altura

	def getArea(self):
		return self._altura * self._base

rectangulo = Rectangulo(15, 20)

# Puedo llamar desde afuera de la clase a los atributos 'privados' que defini en mi clase

print(rectangulo._altura)
print(rectangulo._base)

print(rectangulo.getAltura())
print(rectangulo.getBase())

print(rectangulo.getArea())
