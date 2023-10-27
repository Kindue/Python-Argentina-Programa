# Ejercicio 2: Defina el tipo de dato Estudiante el cual permite almacenar la
# siguiente información: nombre, edad, carrera que cursa. El tipo debe
# permitir:
# 1. Crear estudiante con datos ingresados por el usuario. Cuando se
# desea crear un estudiante sin datos el tipo dispara una excepción.
# 2. Recuperar y modificar los datos usando propiedades.
# 3. Proveer una representación textual de un estudiante.
# 4. Convertir un estudiante a un string.
# 5. Permitir que un estudiante se pueda utilizar como clave en un
# diccionario.
# 6. Comparar estudiantes utilizando los operadores relacionales ==,<,<=,>,>=.


class Estudiante:
    def __init__(self, nb, ed, cr):
        self.nombre = nb
        self.edad = ed
        self.carrera = cr

    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad
    
    def getCarrera(self):
        return self.carrera
    
    def setNombre(self, nuevo):
        self.nombre = nuevo
    
    def setEdad(self, nuevo):
        self.edad = nuevo
    
    def setCarrera(self, nuevo):
        self.carrera = nuevo

    nombre = property(fget= getNombre, fset= setNombre, fdel= None, doc="")
    edad = property(fget= getEdad, fset= setEdad, fdel= None, doc="")
    carrera = property(fget= getCarrera, fset= setCarrera, fdel= None, doc="")

    def __repr__(self):
        aRet = f"Estudiante: \n Nombre: {self.nombre} Edad: {self.edad} Carrera: {self.carrera}"
        return aRet
    
    def __str__(self):
        return self.__repr__()
    
    def __hash__(self):
        return hash(id(self))
    
    def __eq__(self, other):
        return (self.nombre == other.nombre and self.edad == other.edad and self.carrera == other.carrera)
    
    def __lt__(self, other):
        return (self.nombre < other.nombre and self.edad < other.edad and self.carrera < other.carrera)
    
    def __le__(self, other):
        return (self.nombre <= other.nombre and self.edad <= other.edad and self.carrera <= other.carrera)
    
    def __gt__(self, other):
        return (self.nombre > other.nombre and self.edad > other.edad and self.carrera > other.carrera)
    
    def __ge__(self,other):
        return (self.nombre >= other.nombre and self.edad >= other.edad and self.carrera >= other.carrera)
    

carlos = Estudiante("Carlos", 15, "Ing. Quimico")
carlitos = Estudiante("Carlos", 15, "Ing. Quimico")

dicEstudiante = {}

dicEstudiante[carlos] = 1
print(dicEstudiante)
dicEstudiante[carlitos] = 2
print(dicEstudiante)