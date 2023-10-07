# Ejercicio 9: Escriba un programa que genere un diccionario cuya clave sea
# un número natural y cuyo valor sea la tabla de multiplicar correspon-
# diente a la clave.

n = 10
tabla_de_multiplicar = {i: {j: i * j for j in range(1, 11)} for i in range(1, n + 1)}


for clave, valor in tabla_de_multiplicar.items():
    print(f"Tabla de multiplicar del {clave}:")
    for multiplicador, resultado in valor.items():
        print(f"{multiplicador} x {clave} = {resultado}")
    print()