#Ejercicio 4
#Escriba un programa que dada una tupla t con 5 elementos y
#un número n produzca como resultado una nueva tupla con todos los
#elementos de la tupla t multiplicados por el número n.

t = ()
for i in range(5):
	num = int(input("Ingrese un numero para agregar a la tupla: "))
	t += (num,)

n = int(input("Ingrese un numero para multiplicar los elementos de la tupla: "))
resultado = ()

for i in range(5):
	resultado += (t[i] * n,)

print("La tupla resultante de haber multiplicado los elementos de la tupla t por n es la siguiente:", resultado)