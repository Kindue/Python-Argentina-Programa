# Ejercicio 4
# Una Pila es una estructura de datos en donde los datos se
# insertan y suprimen por el tope. Una pila implementa las siguientes
# operaciones:
# 1. Crear crea una pila vacía.
# 2. empty retorna como resultado True si la pila está vacía y False en
# otro caso.
# 3. full retorna como resultado True si la pila está llena y False en
# otro caso.
# 4. push incorpora una un elemento al tope de la pila.
# 5. pop elimina un elemento del tope de la pila.
# 6. top retorna como resultado el elemento que se encuentra en el tope
# de la pila.
# Teniendo en cuenta el funcionamiento de una pila se pide:
# 1. Defina la clase PilaDeEnteros la cual implementa una pila de en-
# teros.
# 2. Implemente las funciones antes mencionadas con las siguientes
# características:
# a) La operación push se realiza con el operador +. Es decir si a
# una pila p se le quiere insertar el número 2 eso se escribe p+2.
# b) La operación de pop se implementa con el operador -. Es decir
# si se desea eliminar un elemento de la pila p el programador
# tiene que escribir p-.
# 3. Además de las operaciones típicas de pila la clase permite:
# a) Comparar si dos pilas son iguales utilizando el operador =.
# b) Proveer una representación de string para una pila.
# c) Calcular la longitud de una pila.


class PilaDeEnteros:
    def __init__(self, tamañoMax):
        self.datos = []
        self.maximo = tamañoMax

    def getPila(self):
        return self.datos

    def __sizeof__(self):
        return len(self.datos)

    def empty(self):
        return self.__sizeof__() == 0
    
    def full(self):
        return self.maximo == self.__sizeof__()
    
    def __add__(self, entero):
        if(self.full()):
            raise ValueError("La pila esta llena, no puedo apilar mas elementos")
        else:
            self.datos.append(entero)

    def __neg__(self):
        if(self.empty()):
            raise ValueError("La pila esta vacia, no puedo desapilar mas elementos")
        else:
            self.datos.pop(self.__sizeof__() - 1)

    def top(self):
        if(self.empty()):
            raise ValueError("La pila esta vacia, no puedo mostrar el elemento del tope de la pila")
        else:
            return self.datos[self.__sizeof__() - 1]
        
    def __eq__(self, pila):
        aRet = True
        if(self.__sizeof__() != pila.__sizeof__()):
            aRet = False
        else:
            for i in range(len(self.datos)):
                if(self.datos[i] != pila.getPila()[i]):
                    aRet = False
                    break
        return aRet
    
    def __str__(self) -> str:
        aRet = "Pila: { "
        for entero in self.datos:
            aRet += f"{entero} "
        aRet += "}"
        return aRet
    

loop = True
dicPilas = {}
while(loop):
    print("A continuacion ingrese la opcion que desee realizar:")
    print("--"*40)
    print("1 : Crear una pila")
    print("--"*40)
    print("2 : Agregar un elemento a una pila")
    print("--"*40)
    print("3 : Consultar si una pila esta vacia")
    print("--"*40)
    print("4 : Consultar si una pila esta llena")
    print("--"*40)
    print("5 : Eliminar el elemento en el tope de una pila")
    print("--"*40)
    print("6 : Obtener el elemento del tope de una pila")
    print("--"*40)
    print("7 : Consultar si dos pilas son iguales")
    print("--"*40)
    print("8 : Consultar la longitud de una pila")
    print("--"*40)
    print("9 : Visualizar pilas agregadas")
    print("--"*40)
    print("0 : Salir")
    print("--"*40)
    op = input()
    if(op == '0'):
        loop = False
    elif(op == '1'):
        print("Ingrese una clave para asociar una pila:")
        clave = input()
        print("Ingrese el tamaño maximo de la pila que desee agregar:")
        try:
            tamaño = int(input())
        except ValueError():
            print("Error al ingresar el tamaño de la pila")
        else:
            nuevaPila = PilaDeEnteros(tamaño)
            dicPilas[clave] = nuevaPila
    elif(op == '2'):
        print("Ingrese la clave asociada a la pila que quiera agregar un elemento:")
        clave = input()
        if(clave not in dicPilas.keys()):
            print("Clave invalida!")
        else:
            try:
                print("Ingrese el entero que quiere agregar:")
                entero = int(input())
            except ValueError():
                print("El elemento ingresado no es un entero!")
            else:
                try:
                    dicPilas[clave] + entero
                except ValueError:
                    print("La pila esta llena, no puedo apilar mas elementos!")
                else:
                    print("Elemento agregado!")
    elif(op == '3'):
        print("Ingrese la clave asociada a la pila a consultar si esta vacia:")
        clave = input()
        if(clave not in dicPilas.keys()):
            print("Clave invalida!")
        else:
            if(dicPilas[clave].empty()):
                print("La pila esta vacia!")
            else:
                print("La pila tiene elementos!")
    elif(op == '4'):
        print("Ingrese la clave asociada a la pila a consultar si esta llena:")
        clave = input()
        if(clave not in dicPilas.keys()):
            print("Clave invalida!")
        else:
            if(dicPilas[clave].full()):
                print("La pila esta llena!")
            else:
                print("La pila NO esta llena!")
    elif(op == '5'):
        print("Ingrese la clave asociada a la pila que quiere eliminar su tope:")
        clave = input()
        if(clave not in dicPilas.keys()):
            print("Clave invalida!")
        else:
            try:
                -dicPilas[clave]
            except ValueError():
                print("La pila esta vacia, no puedo desapilar mas elementos")
            else:
                print("Tope de la pila eliminado!")
    elif(op == '6'):
        print("Ingrese la clave asociada a la pila que quiere revisar su tope:")
        clave = input()
        if(clave not in dicPilas.keys()):
            print("Clave invalida!")
        else:
            try:
                print("El elemento en el tope de la pila es:", dicPilas[clave].top())
            except ValueError():
                print("La pila esta vacia, no puedo mostrar el elemento del tope de la pila")
    elif(op == '7'):
        print("Ingrese la clave asociada a la pila que quiere comparar si es igual a otra:")
        clave1 = input()
        print("Ingrese la clave asociada a la otra pila que quiere comparar si es igual a la ingresada:")
        clave2 = input()
        if(clave1 not in dicPilas.keys() or clave2 not in dicPilas.keys()):
            print("Alguna de las claves ingresadas es invalida!")
        else:
            if(dicPilas[clave1] == dicPilas[clave2]):
                print("Las pilas son iguales!")
            else:
                print("Las pilas no son iguales!")
    elif(op == '8'):
        print("Ingrese la clave asociada a la pila que quiere conocer su longitud:")
        clave = input()
        if(clave not in dicPilas.keys()):
            print("Clave invalida!")
        else:
            print("La pila ingresada contiene", dicPilas[clave].__sizeof__(), "elementos")
    elif(op == '9'):
        for clave in dicPilas.keys():
            print("Pila", clave)
            print(dicPilas[clave])
    else:
        print("Opcion invalida")