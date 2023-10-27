# Ejercicio 16: Realice las siguientes actividades:
# 1. Diseñe una representación para un árbol ternario. Un árbol ter-
# nario es aquel donde la máxima cantidad de hijos por nodo es
# 3.
# 2. Implemente los siguientes recorridos:
# a) Simétrico
# b) Post orden
# c) Pre orden

class ArbolTernarioNodo:
    def __init__(self, dato, padre=None, hijoDer=None, hijoMedio=None, hijoIzq=None):
        self.dato = dato
        self.padre = padre
        self.hijoDer = hijoDer
        self.hijoMedio = hijoMedio
        self.hijoIzq = hijoIzq

    def getDato(self):
        return self.dato
    def getPadre(self):
        return self.padre
    def getHijoDerecho(self):
        return self.hijoDer
    def getHijoMedio(self):
        return self.hijoMedio
    def getHijoIzquierdo(self):
        return self.hijoIzq
    
    def setDato(self, nuevo):
        self.dato = nuevo
    def setPadre(self, nuevo):
        self.padre = nuevo
    def setHijoDerecho(self, nuevo):
        self.hijoDer = nuevo
    def setHijoMedio(self, nuevo):
        self.hijoMedio = nuevo
    def setHijoIzquierdo(self, nuevo):
        self.hijoIzq = nuevo

class ArbolTernario:
    def __init__(self):
        self.raiz = None
        self.tamaño = 0

    def getRaiz(self):
        if(self.raiz == None):
            raise TypeError("El arbol esta vacio")
        return self.raiz
    
    def getSize(self):
        return self.tamaño
    
    def tieneDerecho(self, padre):
        return padre.getDerecho() != None
    
    def tieneMedio(self, padre):
        return padre.getMedio() != None
    
    def tieneIzquierdo(self, padre):
        return padre.getIzquierdo() != None
    
    def nodoIzquierdo(self, padre):
        aRet = None
        if(padre.getHijoIzquierdo() != None):
            aRet = padre.getHijoIzquierdo()
        return aRet
    
    def nodoMedio(self, padre):
        aRet = None
        if(padre.getHijoMedio() != None):
            aRet = padre.getHijoMedio()
        return aRet
    
    def nodoDerecho(self, padre):
        aRet = None
        if(padre.getHijoDerecho() != None):
            aRet = padre.getHijoDerecho()
        return aRet
    
    def setRaiz(self, dato):
        if(self.raiz != None):
            raise TypeError("No puedo cambiar la raiz")
        self.raiz = ArbolTernarioNodo(dato)
        self.tamaño += 1
    
    def insertarNodoDerecho(self, padre, dato):
        if(padre.getHijoDerecho() != None):
            raise TypeError("Ya hay un hijo derecho, no puedo insertar otro")
        else:
            nuevoNodo = ArbolTernarioNodo(dato, padre)
            padre.setHijoDerecho(nuevoNodo)
            self.tamaño += 1
            return nuevoNodo
    
    def insertarNodoMedio(self, padre, dato):
        if(padre.getHijoMedio() != None):
            raise TypeError("Ya hay un hijo medio, no puedo insertar otro")
        else:
            nuevoNodo = ArbolTernarioNodo(dato, padre)
            padre.setHijoMedio(nuevoNodo)
            self.tamaño += 1
            return nuevoNodo
    
    def insertarNodoIzquierdo(self, padre, dato):
        if(padre.getHijoIzquierdo() != None):
            raise TypeError("Ya hay un hijo izquierdo, no puedo insertar otro")
        else:
            nuevoNodo = ArbolTernarioNodo(dato, padre)
            padre.setHijoIzquierdo(nuevoNodo)
            self.tamaño += 1
            return nuevoNodo

    def removerNodo(self, nodo):
        if(self.tamaño == 0):
            raise TypeError("El arbol esta vacio, no puedo remover nada")
        if((self.tieneIzquierdo(nodo) and self.tieneMedio(nodo)) or (self.tieneIzquierdo(nodo) and self.tieneDerecho(nodo)) or (self.tieneMedio(nodo) and self.tieneDerecho(nodo))):
            raise TypeError("No puedo remover el nodo porque tiene mas de un hijo")
        
        if(self.tieneIzquierdo(nodo)):
            hijo = nodo.getIzquierdo()
        elif(self.tieneMedio(nodo)):
            hijo = nodo.getMedio()
        elif(self.tieneIzquierdo(nodo)):
            hijo = nodo.getDerecho()
        else:
            hijo = None

        if(nodo == self.getRaiz()):
            if(hijo != None):
                hijo.setPadre(None)
            self.raiz = hijo
        else:
            padre = nodo.getPadre()
            if(padre.getHijoDerecho() == nodo):
                padre.setHijoDerecho(hijo)
            elif(padre.getHijoMedio() == nodo):
                padre.setHijoMedio(hijo)
            else:
                padre.setHijoIzquierdo(hijo)
            if(hijo != None):
                hijo.setPadre(padre)
        self.tamaño -= 1

def preOrden(arbol, nodo):
    if(nodo != None):
        print(nodo.getDato(), end=", ")
        preOrden(arbol, arbol.nodoIzquierdo(nodo))
        preOrden(arbol, arbol.nodoMedio(nodo))
        preOrden(arbol, arbol.nodoDerecho(nodo))

def posOrden(arbol, nodo):
    if(nodo != None):
        posOrden(arbol, arbol.nodoIzquierdo(nodo))
        posOrden(arbol, arbol.nodoMedio(nodo))
        posOrden(arbol, arbol.nodoDerecho(nodo))
        print(nodo.getDato(), end=", ")

def inOrden(arbol, nodo):
    if(nodo != None):
        posOrden(arbol, arbol.nodoIzquierdo(nodo))
        print(nodo.getDato(), end=", ")
        posOrden(arbol, arbol.nodoMedio(nodo))
        # print(nodo.getDato(), end=", ")
        posOrden(arbol, arbol.nodoDerecho(nodo))


arbol = ArbolTernario()
arbol.setRaiz(0)
A = arbol.getRaiz()
B = arbol.insertarNodoIzquierdo(A, 1)
C = arbol.insertarNodoMedio(A, 2)
D = arbol.insertarNodoDerecho(A, 3)

E = arbol.insertarNodoIzquierdo(B, 4)
F = arbol.insertarNodoMedio(B, 5)
G = arbol.insertarNodoDerecho(B, 6)

H = arbol.insertarNodoIzquierdo(C, 7)
I = arbol.insertarNodoMedio(C, 8)
J = arbol.insertarNodoDerecho(C, 9)

K = arbol.insertarNodoIzquierdo(D, 10)
L = arbol.insertarNodoMedio(D, 11)
M = arbol.insertarNodoDerecho(D, 12)

N = arbol.insertarNodoIzquierdo(E, 13)
Ñ = arbol.insertarNodoMedio(E, 14)
O = arbol.insertarNodoDerecho(E, 15)
P = arbol.insertarNodoIzquierdo(F, 16)
Q = arbol.insertarNodoMedio(F, 17)
R = arbol.insertarNodoDerecho(F, 18)
S = arbol.insertarNodoIzquierdo(G, 19)

V = arbol.insertarNodoIzquierdo(H, 20)
T = arbol.insertarNodoMedio(H, 21)
U = arbol.insertarNodoDerecho(I, 22)

W = arbol.insertarNodoMedio(K, 23)
X = arbol.insertarNodoIzquierdo(L, 24)
Y = arbol.insertarNodoMedio(M, 25)
Z = arbol.insertarNodoDerecho(M, 26)

print("Preorden del arbol:")
preOrden(arbol, A)
print("\n")
print("--"*40)
print("PosOrden del arbol")
posOrden(arbol, A)
print("\n")
print("--"*40)
print("InOrden del arbol")
inOrden(arbol, A)