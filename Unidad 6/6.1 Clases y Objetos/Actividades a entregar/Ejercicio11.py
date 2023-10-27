# Ejercicio 11: Realice las siguientes actividades:
# 1. Defina la clase Animal la cual permite almacenar el grupo al cual
# pertenece el animal: Vertebrado, Invertebrado, Anélidos, Molus-
# cos, Poríferos, Cnidarios, Nematodos, Platelmintos .
# 2. Defina la clase Perro la cual permite almacenar la raza de un perro.
# 3. Defina la clase Pez la cual permite almacenar si es de agua dulce
# o salada.
# 4. Escriba un programa principal que permita:
#     Almacenar en una lista perros y peces.
#     Imprimir la lista


class Animal:
    def __init__(self, gr):
        self.grupo = gr

    def getGrupo(self):
        return self.grupo
    
    def setGrupo(self, nuevo):
        self.grupo = nuevo

    def imprimir(self):
        print("Grupo:", self.grupo)

class Perro(Animal):
    def __init__(self, rz):
        super().__init__("Vertebrado")
        self.raza = rz

    def getRaza(self):
        return self.raza
    
    def setRaza(self, nuevo):
        self.raza = nuevo

    def imprimir(self):
        super().imprimir()
        print("Perro raza", self.raza)

class Pez(Animal):
    def __init__(self, agua):
        super().__init__("Vertebrado")
        self.tipoAgua = agua

    def getTipoAgua(self):
        return self.tipoAgua
    
    def setTipoAgua(self, nuevo):
        self.tipoAgua = nuevo

    def imprimir(self):
        super().imprimir()
        print("Pez de agua", self.tipoAgua)

listaAnimales = []

def ingresarAnimal(tipo):
    if(tipo == '1'):
        print("Ingrese la raza del perro que desee agregar:")
        raza = input()
        nuevoAnimal = Perro(raza)
    else:
        print("Ingrese de que tipo de agua es el pez que desee agregar:")
        tipoAgua = input()
        nuevoAnimal = Pez(tipoAgua)
    listaAnimales.append(nuevoAnimal)

loop = True
while(loop):
    print("A continuacion ingrese el tipo de animal que desee agregar:")
    print("--"*40)
    print("1 : Perro")
    print("--"*40)
    print("2 : Pez")
    print("--"*40)
    print("0 : Salir")
    print("--"*40)
    tipoAnimal = input()
    if(tipoAnimal == '1' or tipoAnimal == '2'):
        ingresarAnimal(tipoAnimal)
    elif(tipoAnimal == '0'):
        loop = False
    else:
        print("Ingreso una opcion incorrecta, vuelva a intentarlo")


print("La lista de animales con su informacion es la siguiente:")
for animal in listaAnimales:
    animal.imprimir()
    print("--"*40)