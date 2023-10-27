# Ejercicio 6
# Defina la clase MatrizCuadrada la cual permite almacenar nú-
# meros flotantes. La clase permite realizar las siguientes operaciones:
# 1. Cargar una matriz.
# 2. Asignar a una variable una matriz.
# 3. Sumar dos matrices.
# 4. Restar dos matrices.
# 5. Construir una representación textual de una matriz.
# Nota: Para resolver este ejercicio sobrecargue los operadores que crea
# conveniente.


class MatrizCuadrada:
    def __init__(self, n):                                   #Crea una lista de n listas, cada lista interna tiene 
        self._tamaño = n                                     #n entradas, inicializa todos los valores en 0
        self._matriz = [[0 for i in range(self._tamaño)] for j in range(self._tamaño)]

    @property
    def getTamaño(self):
        return self._tamaño
    
    @property
    def getMatriz(self):
        return self._matriz
    
    def cargarMatriz(self, elementos):
        if(len(elementos) != self._tamaño * self._tamaño):
            raise ValueError("La cantidad de elementos no es la misma que el tamaño de la matriz")
        aux = 0
        for i in range(self._tamaño):
            for j in range(self._tamaño):
                self._matriz[i][j] = elementos[aux]
                aux += 1

    def __add__(self, matrizAux):
        if(matrizAux._tamaño != self._tamaño):
            raise ValueError("No puedo sumar matrices cuadradas con distintos tamaños")
        matrizResultado = MatrizCuadrada(self._tamaño)
        for i in range(self._tamaño):
            for j in range(self._tamaño):
                matrizResultado._matriz[i][j] = self._matriz[i][j] + matrizAux._matriz[i][j]
        return matrizResultado
    
    def __sub__(self, matrizAux):
        if(matrizAux._tamaño != self._tamaño):
            raise ValueError("No puedo restar matrices cuadradas con distintos tamaños")
        matrizResultado = MatrizCuadrada(self._tamaño)
        for i in range(self._tamaño):
            for j in range(self._tamaño):
                matrizResultado[i][j] = self._matriz[i][j] - matrizAux._matriz[i][j]
        return matrizResultado
    
    def __str__(self):
        matrizSTR = ""
        for i in range(self._tamaño):
            matrizSTR += "| "
            for j in range(self._tamaño):
                matrizSTR += f"{self._matriz[i][j]}  "
            matrizSTR += " |\n"
        return matrizSTR
    

def ingresarElementos(matriz):
    lista = []
    print("A continuacion ingrese los valores en orden para cargar la matriz")
    n = matriz._tamaño
    for i in range(n * n):
        print("Ingrese un numero a agregar a la matriz:")
        num = float(input())
        lista.append(num)
    matriz.cargarMatriz(lista)

loop = True
dicMatrices = {}
while(loop):
    print("A continuacion ingrese la opcion que desee realizar:")
    print("--"*40)
    print("1 : Agregar matriz")
    print("--"*40)
    print("2 : Sumar matrices")
    print("--"*40)
    print("3 : Restar matrices")
    print("--"*40)
    print("4 : Visualizar matrices")
    print("--"*40)
    print("0 : Salir")
    print("--"*40)
    op = input()
    if(op == '0'):
        loop = False
    elif(op == '1'):
        print("Ingrese una clave para asociar una matriz:")
        clave = input()
        print("Ingrese el tamaño de filas que quiere tener la nueva matriz")
        try:
            tamaño = int(input())
        except TypeError():
            print("Error al ingresar el tamaño de filas")
        else:
            nuevaMatriz = MatrizCuadrada(tamaño)
            ingresarElementos(nuevaMatriz)
            dicMatrices[clave] = nuevaMatriz
    elif(op == '2'):
        print("Ingrese la clave asociada una de las dos matrices a sumar:")
        clave1 = input()
        print("Ingrese la clave asociada a la segunda matriz a sumar:")
        clave2 = input()
        matrizResultado = dicMatrices[clave1] + dicMatrices[clave2]
        print("El resultado de la suma de las dos matrices es el siguiente:")
        print(matrizResultado)
        print("Desea guardar el resultado? Ingrese 0 para guardar, cualquier otra tecla para volver al menu principal")
        opSum = input()
        if(opSum == '0'):
            print("Ingrese una clave para asociar una matriz:")
            clave = input()
            dicMatrices[clave] = matrizResultado
    elif(op == '3'):
        print("Ingrese la clave asociada una de las dos matrices a restar:")
        clave1 = input()
        print("Ingrese la clave asociada a la segunda matriz a restar:")
        clave2 = input()
        matrizResultado = dicMatrices[clave1] - dicMatrices[clave2]
        print("El resultado de la resta de las dos matrices es el siguiente:")
        print(matrizResultado)
        print("Desea guardar el resultado? Ingrese 0 para guardar, cualquier otra tecla para volver al menu principal")
        opRes = input()
        if(opRes == '0'):
            print("Ingrese una clave para asociar una matriz:")
            clave = input()
            dicMatrices[clave] = matrizResultado
    elif(op == '4'):
        for key in dicMatrices.keys():
            print(key + "  :  ")
            print(dicMatrices[key])
    else:
        print("Opcion Invalida!")