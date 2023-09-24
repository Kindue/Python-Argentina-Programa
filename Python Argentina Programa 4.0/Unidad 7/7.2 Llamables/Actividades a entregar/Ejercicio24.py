# Ejercicio 24: Defina la función generarÁrea la cual tiene tres parámetros
# el primero indica qué área quiere generar si la de un triángulo o la
# de un rectángulo. Los parámetros restantes son la base y la altura. A
# continuación se muestran ejemplos de uso de la función:
# t1=generarÁrea(True,2,3)
# r1=generarÁrea(True,2,2)
# print(" Área del Triángulo:",t1)
# print(" Área del Rectángulo:",r1)


def generarArea(esTriangulo, base, altura):
    if(esTriangulo):
        return (base * altura) / 2
    else:
        return base * altura
    

t1 = generarArea(True, 2, 3)
r1 = generarArea(False, 2, 2)
print("Área del Triángulo:", t1)
print("Área del Rectángulo:", r1)