# Ejercicio 16: Defina un generador que produzca los divisores de un número
# ingresado por el usuario.

def generador_divisores(numero):
    for i in range(1, numero + 1):
        if numero % i == 0:
            yield i

numero_ingresado = int(input("Ingrese un número para generar sus divisores: "))

divisores_generador = generador_divisores(numero_ingresado)

print(f"Divisores de {numero_ingresado}:")
for divisor in divisores_generador:
    print(divisor)