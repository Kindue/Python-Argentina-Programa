# Ejercicio 3: Defina una función recursiva que permita calcular el mcd de
# dos números.
# Nota: Utilice el Algoritmo de Euclides.


def mcd(a, b):
    if(a < b):
        aux = b
        b = a
        a = aux
    return mcdAux(a, b)

def mcdAux(a, b):
    if(b == 0):
        return a
    else:
        return mcdAux(b, a % b)
    
try:
    print("Ingrese dos numeros para calcular su maximo comun divisor:")
    num1 = int(input())
    num2 = int(input())
except ValueError():
	print("No ingreso un numero, adios!")

if(num1 < 0 or num2 < 0):
    num1 = abs(num1)
    num2 = abs(num2)

print("El maximo comun divisor entre", num1, "y", num2, "es el siguiente")
print(f"mcd({num1}, {num2}) = {mcd(num1, num2)}")