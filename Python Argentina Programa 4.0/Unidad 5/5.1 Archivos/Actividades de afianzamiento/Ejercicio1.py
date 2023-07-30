#Ejercicio 1
#Escriba un programa que permita que el usuario ingrese el
#nombre de un archivo el programa lee el contenido y lo imprime por
#pantalla.


loop = True
while(loop):
    try:
        print("Ingrese la ruta del archivo que desee leer por pantalla: ")
        archivo = open(str(input()))
        contenido = archivo.read()
        print(contenido)
        archivo.close()
        loop = False
    except ValueError:
        print("Se ingreso una ruta incorrecta, vuelva a intentarlo!")
    except FileNotFoundError:
        print("La ruta del archivo ingresada no coincide con ningun archivo existente, vuelva a intentarlo!")