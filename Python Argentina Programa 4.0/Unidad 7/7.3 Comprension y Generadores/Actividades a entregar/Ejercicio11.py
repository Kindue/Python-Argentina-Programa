# Ejercicio 11: Defina un generador que genere palíndromos numéricos.

def generarPalindromos(n):
    palindromos = (int(str(num) + str(num)[::-1]) for num in range(1, n + 1))
    return palindromos

n = 100
generador = generarPalindromos(n)

for i in range(10):
    print(next(generador))