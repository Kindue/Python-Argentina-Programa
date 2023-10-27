# Ejercicio 18: Escriba una función que retorne como resultado otra función
# la cual permite pasar un string a mayúsculas.


def crearFuncionMayusculas():
    return lambda cadena: cadena.upper()

convertirAMayusculas = crearFuncionMayusculas()

cadena = "Se viene la 7ma!"

print(cadena)

print(convertirAMayusculas(cadena))