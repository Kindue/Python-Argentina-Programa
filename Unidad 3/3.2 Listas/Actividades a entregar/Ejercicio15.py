#Ejercicio 15
#Dada la lista l=[34, 3.2, "Juan", "Pedro",-2] se pide:
#1. Agregue al final de l un string ingresado por el usuario.
#2. Solicite al usuario un elemento y cuente la cantidad de veces que
#aparece dicho elemento en l.
#3. Pida al usuario una lista s e incorporela al final de l.
#4. Invierta la lista l.


l = [34, 3.2, "Juan", "Pedro",-2]

for i in range(len(l)):                                                   #Paso la lista original a string
	l[i] = str(l[i])													  #asi puedo contar los elementos que												
																		  #no son string
l.append(input("Ingrese un String para agregarlo al final de la lista: "))

a = input("Ingrese un elemento a buscar cuantas veces aparece en la lista: ")
veces = l.count(a)

print()
print("El elemento", a, "aparecio", veces, "veces en la lista original")
print()

s = input("Ingrese una lista s separando cada elemento con un espacio: ").split()
l = l + s

print()
print("La lista l ahora tiene los elementos de la lista s:", l)
print()

l.reverse()

print("Asi quedo la lista l luego de agregarle la lista s nueva al final e invertirla:")
print()
print(l)