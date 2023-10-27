# Ejercicio 14: Defina un generador que produzca los múltiplos de un número
# ingresado por el usuario.


def generador_multiplos(numero):
    contador = 1
    while True:
        yield numero * contador
        contador += 1

numero_ingresado = int(input("Ingrese un número para generar sus múltiplos: "))

multiplos_generador = (numero_ingresado * i for i in range(1, 6)) 

for multiplo in multiplos_generador:
    print(multiplo)