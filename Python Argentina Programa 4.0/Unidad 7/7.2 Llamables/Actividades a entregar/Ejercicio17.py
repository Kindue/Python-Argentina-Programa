# Ejercicio 17: Defina funciones lambda para:
# 1. Calcular el doble de un número.
# 2. Determinar si un número es impar.
# 3. Dados dos strings retornar el de mayor longitud.
# 4. Dada una dupla retornar otra cuya primera componente sea el
# doble de la primer componente de la dupla de entrada y el segundo
# ítem sea el triple del segundo ítem de la dupla de entrada.
# 5. Determinar si un número es mayor que 0.
# 6. Determinar si un número está dentro de un rango determinado.
# 7. Determinar si un punto está dentro de una circunsferencia.
# 8. Calcular el área de un triángulo.
# 9. Calcular el área de un cuadrado.
# 10. Ordenar de forma ascendente o descendente una lista de números
# enteros.


dobleDeN = lambda n: 2 * n
esImpar = lambda n: n % 2 == 1
mayorString = lambda s, t: s if(len(s) >= len(t)) else t
nuevaTupla = lambda t: (t[0] * 2, t[1] * 3)
mayorACero = lambda n: n > 0
dentroRango = lambda x, y, n: x <= n <= y
dentroCircunferencia = lambda x, y, centroX, centroY, radio: (x-centroX)**2 + (y-centroY)**2 <= radio**2
areaTriangulo = lambda b, h: (b * h) / 2
areaCuadrado = lambda l: l * 2
ordenaLista = lambda l: l.sort()

print("El doble de 3,5 es:", dobleDeN(3.5))
print("¿El 7 es impar?", esImpar(7))
print("¿Bokita tiene mas letras que Septima?", mayorString("Bokita", "Septima"))
print("El doble de la primer componente y el triple de la segunda componente de la siguiente tupla: (4, 9)", nuevaTupla((4, 9)))
print("¿El 7 es mayor a 0?", mayorACero(7))
print("¿El 7 esta dentro del siguiente rango: [-28, 4]?", dentroRango(-28, 4, 7))
print("¿El punto (7, 7) esta dentro de la circunferencia con centro en (0, 0) y radio 4?", dentroCircunferencia(7,7,0,0,4))
print("El area del triangulo con base de 7cm y altura de 7cm es:", areaTriangulo(7,7))
print("El area del cuadrado de lado de 7cm es:", areaCuadrado(7))
lista = [5,2,6,7,2,7,0,1]
print(f"La lista {lista} cuando esta ordenada es la siguiente lista:")
ordenaLista(lista)
print(lista)