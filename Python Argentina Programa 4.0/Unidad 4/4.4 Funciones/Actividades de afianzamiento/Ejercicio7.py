#Ejercicio 7
#Dado el siguiente programa:
#def maximo ( x , y ) :
#return x i f x>y e l s e : y
#def minimo ( x , y ) :
#return x i f x<y e l s e : y
##programa p r i n c i p a l
#x=int ( input ( "Un␣número : ␣" ) )
#y=int ( input ( " Otro ␣número : ␣" ) )
#print ( maximo ( x−3, minimo ( x+2, y −5)))
#Se pide:
#1. De un ejemplo de ejecución del programa.
#2. Diga que hace el programa.
#3. Critique la organización del código.


def maximo(x, y):
	return x if(x>y) else y

def minimo(x, y):
	return x if(x<y) else y

#programa principal

x = int(input("Un numero: "))
y = int(input("Otro numero: "))
print(maximo(x-3, minimo(x+2, y-5)))

#Ejemplo de ejecucion con x = 5 e y = 7
#
#Un numero: 5
#Otro numero: 7
#2

#Explicacion del programa
#Las funciones calculas el maximo y el minimo respectivamente entre los numeros que son pasados por parametros.
#El programa principal pide dos numeros al usuario y luego calcular el maximo entre el primer numero restado a 3
#y el minimo entre el primer numero sumado 2 y el segundo numero restando 5, luego lo imprime.


#El codigo es corto pero no muy legible, los minimos y maximos calculados podrian ser calculados en variables
#extras realizando tambien las sumas y restas para favorecer este problema