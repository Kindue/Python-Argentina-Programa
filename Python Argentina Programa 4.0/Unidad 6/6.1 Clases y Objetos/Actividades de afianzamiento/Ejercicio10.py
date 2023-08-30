# Ejercicio 10
# A través del análisis de las clases definidas en los ejercicio 7
# y 8 y en programa creado en 9 elabore una solución con la utilización
# de herencia. Luego compare las soluciones.


class Empleado:
	def __init__(self, nb, tr):
		self.nombre = nb
		self.lugar = tr

	def getNombre(self):
		return self.nombre

	def getLugar(self):
		return self.lugar

	def setNombre(self, nuevo):
		self.nombre = nuevo
		
	def setLugar(self, nuevo):
		self.lugar = nuevo
		
	def dineroTotal(self):
		pass
		
class EmpleadoExclusivo (Empleado):
	def __init__(self, nb, tr, sueldo):
		super().__init__(nb, tr)
		self.sueldo = sueldo
	
	def getSueldo(self):
		return self.sueldo
		
	def setSueldo(self, nuevo):
		self.sueldo = nuevo
		
	def dineroTotal(self):
		return self.getSueldo()
        

class EmpleadoPorHora(Empleado):
	def __init__(self, nb, tr, precio, ht):
		super().__init__(nb, tr)
		self.pph = precio
		self.cantH = ht

	def getPrecio(self):
		return self.pph

	def getCantH(self):
		return self.cantH

	def setPrecio(self, nuevo):
		self.pph = nuevo

	def setCantH(self, nuevo):
		self.cantH = nuevo

	def dineroTotal(self):
		return (self.pph * self.cantH)
	
listaEmpleados = []

def ingresarPersona(tipo):
    try:
        print("Ingrese el nombre de un nuevo empleado a agregar:")
        nombre = input()
        print("Ingrese el nombre del lugar de trabajo de este empleado:")
        lugar = input()
        if(tipo == '1'):
            print("Ingrese el precio por hora de trabajo de este empleado:")
            pph = float(input())
            print("Ingrese la cantidad de horas trabajadas por esta persona:")
            cantH = int(input())
            nuevoEmpleado = EmpleadoPorHora(nombre, lugar, pph, cantH)
        if(tipo == '2'):
            print("Ingrese el sueldo del empleado exclusivo:")
            sueldo = float(input())
            nuevoEmpleado = EmpleadoExclusivo(nombre, lugar, sueldo)
        listaEmpleados.append(nuevoEmpleado)
    except ValueError:
        print("Se ingreso una edad no valida, no se pudo agregar a esa persona!")

loop = True
while(loop):
    print("A continuacion ingrese el tipo de empleado que desee agregar:")
    print("--"*40)
    print("1 : Empleado por hora")
    print("--"*40)
    print("2 : Empleado exclusivo")
    print("--"*40)
    print("0 : Salir")
    print("--"*40)
    tipoEmpleado = input()
    if(tipoEmpleado == '1' or tipoEmpleado == '2'):
        ingresarPersona(tipoEmpleado)
    elif(tipoEmpleado == '0'):
        loop = False
    else:
        print("Ingreso una opcion incorrecta, vuelva a intentarlo")

mayorDinero = 0

for empleado in listaEmpleados:
    if(empleado.dineroTotal() >= mayorDinero):
        mayorDinero = empleado.dineroTotal()

print("La mayor cantidad de dinero que ganan los empleados ingresados en la lista es:", mayorDinero)
print("--"*40)