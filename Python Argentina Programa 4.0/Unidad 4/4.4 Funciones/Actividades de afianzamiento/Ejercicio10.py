#Ejercicio 10
#Construya una función que reciba como parámetro dos valores
#si esos valores son enteros la función retorna como resultado la suma
#de dichos valores. Si los valores son strings la función retorna como
#resultado la concatenación de los strings. En otro caso la función dispara
#una excepción ValueError.


def suma(v1, v2):
	try:
		resultado = v1 + v2
	except ValueError:
		print("Una de las variables no es del mismo tipo que la otra!")
	else:
		return resultado

print("Ingrese el primer valor: ")
ele1 = input()
print("Ingrese el segundo valor: ")
ele2 = input()
try:
	ele1 = int(ele1)
	ele2 = int(ele2)
except:
	pass
finally:
	print(suma(ele1, ele2))