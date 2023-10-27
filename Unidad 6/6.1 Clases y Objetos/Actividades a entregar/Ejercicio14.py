# Ejercicio 14
# Realice las siguientes actividades:
# 1. Defina la clase Empresa la cual permite registrar el nombre de la
# empresa, dirección y cuit.
# 2. Defina la clase RenglónDeFactura. La clase registra la siguiente
# información:
# a) Cantidad de unidades de una mercadería.
# b) La descripción de la mercadería.
# c) El precio unitario la mercadería.
# d ) El precio total (todas las unidades de la mercadería).
# 3. Defina la clase Factura, la que permite registrar el número de la
# factura, la empresa, las mercaderías que compran, también per-
# mite calcular el total sin un porcentaje de IVA, el porcentaje de
# IVA y el total con IVA.
# 4. Escriba un programa principal que permita que:
# a) El usuario ingrese n facturas y las almacene en una diccionario
# de facturas. El número de la factura es la clave y la factura
# en si es el valor.
# b) Imprima el nombre del cliente que hizo la mayor compra.
# c) Imprima el total de ventas.
# d) Imprima todos los números de facturas.


class Empresa:
    def __init__(self, nombre, direccion, cuit):
        self.nombre = nombre
        self.direccion = direccion
        self.cuit = cuit
    
    def getNombre(self):
        return self.nombre
    
    def getDireccion(self):
        return self.direccion
    
    def getCUIT(self):
        return self.cuit
    
    def setNombre(self, nuevo):
        self.nombre = nuevo

    def setDireccion(self, nuevo):
        self.direccion = nuevo

    def setCUIT(self, nuevo):
        self.cuit = nuevo

    def imprimir(self):
        print(self.nombre, "", self.direccion, "", self.cuit)

class RenglonDeFactura:
    def __init__(self, cantUD, descripcion, precioUD):
        self.descripcion = descripcion
        self.cantUD = cantUD
        self.precioUD = precioUD
        self.precioTotal = self.cantUD * self.precioUD

    def getDescripcion(self):
        return self.descripcion

    def getCantUD(self):
        return self.cantUd
    
    def getPrecioUD(self):
        return self.precioUd
    
    def getPrecioTotal(self):
        return self.precioTotal
    
    def setDescripcion(self, nuevo):
        self.descripcion = nuevo

    def setCantUD(self, nuevo):
        self.cantUD = nuevo

    def setPrecioUD(self, nuevo):
        self.precioUD = nuevo

class Factura:
    def __init__(self, nroFactura, empresa, listaMercaderia, IVA):
        self.nroFactura = nroFactura
        self.empresa = empresa
        self.listaMercaderia = listaMercaderia
        self.IVA = IVA

    def getNroFactura(self):
        return self.nroFactura
    
    def getEmpresa(self):
        return self.empresa
    
    def getMercaderia(self):
        return self.listaMercaderia
    
    def getIVA(self):
        return self.IVA
    
    def setNroFactura(self, nuevo):
        self.nroFactura = nuevo

    def setEmpresa(self, nuevo):
        self.empresa = nuevo

    def setListaMercaderia(self, nuevo):
        self.listaMercaderia = nuevo

    def setIVA(self, nuevo):
        self.IVA = nuevo

    def calculoTotal(self):
        sumaTotal = 0
        for renglon in self.listaMercaderia:
            sumaTotal += renglon.getPrecioTotal()
        return sumaTotal
    
    def calculoTotalConIVA(self):
        return self.calculoTotal() * self.IVA
    
def ingresarEmpresa():
    loop = True
    while(loop):
        try:
            print("Complete con la informacion de la empresa")
            print("Ingrese el nombre de la empresa:")
            nombre = input()
            print("Ingrese la direccion legal de la empresa:")
            direccion = input()
            print("Ingrese el CUIT de la empresa:")
            cuit = int(input())
            loop = False
        except ValueError():
            print("Ingreso un CUIT invalido, vuelva a intentarlo!")
    return Empresa(nombre, direccion, cuit)

def ingresarMercaderia():
    listaARet = []
    loop = True
    while(loop):
        try:
            print("Complete la informacion de un producto en un nuevo renglon de la factura")
            print("Ingrese la descripcion de el producto:")
            descripcion = input()
            print("Ingrese la cantidad de unidades del producto en la factura:")
            cantUD = int(input())
            print("Ingrese el precio de cada unidad del producto:")
            precioUD = float(input())
            nuevoRenglon = RenglonDeFactura(descripcion, cantUD, precioUD)
            listaARet.append(nuevoRenglon)
            print("Producto agregado, desea agregar mas productos? Ingrese 0 para salir, o cualquier otra tecla para continuar")
            opcion = input()
            if(opcion == '0'):
                loop = False
        except ValueError():
            print("Ingreso un dato incorrecto, vuelva a intentarlo!")
    return listaARet

################ Programa principal ##################

loopPrincipal = True
diccionarioFacturas = {}
while(loopPrincipal):
    print("A continuacion ingrese los datos de la factura que desee agregar!")
    print("Ingrese el numero de la factura a ingresar:")
    nroFactura = input()
    empresa = ingresarEmpresa()
    listaMercaderia = ingresarMercaderia()
    print("Ingrese el porcentaje del IVA a agregar en el valor de cada producto:")
    IVA = input()
    nuevaFactura = Factura(nroFactura, empresa, listaMercaderia, IVA)
    diccionarioFacturas[nroFactura] = nuevaFactura
    print("Factura creada, desea ingresar mas facturas? Ingrese 0 para salir, o cualquier otra tecla para continuar")
    opcion = input()
    if(opcion == '0'):
        loopPrincipal = False

total = 0
mayor = 0
print("--"*40)
print("A continuacion se mostraran todos los numeros de facturas en el diccionario de facturas:")
print("--"*40)
for factura in diccionarioFacturas:
    if(factura.calculoTotalConIVA() > mayor):
        mayor = factura.calculoTotalConIVA()
        empresaMayor = factura.getEmpresa()
    total += factura.calculoTotalConIVA()
    print(factura.getNroFactura())
    print("--"*40)

print("El total de ventas en todas las facturas del diccionario es: $", total)
print("--"*40)
print("La empresa que hizo la mayor compra tiene los siguientes datos:")
print("--"*40)
empresaMayor.imprimir()
print("--"*40)