#Ejercicio 1
#Escriba un programa que:
#1. Defina el conjunto universal el cual contiene las provincias de Ar-
#gentina.
#2. Pida al usuario una provincia.
#3. Calcule el complemento del conjunto single que contiene la pro-
#vincia ingresada por el usuario.

conjunto_universal = frozenset({"Buenos Aires", "Ciudad Autónoma de Buenos Aires", "Catamarca", "Chaco", "Chubut",
        "Córdoba", "Corrientes", "Entre Ríos", "Formosa", "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones",
        "Neuquén", "Río Negro", "Salta", "San Juan", "San Luis", "Santa Cruz", "Santa Fe", "Santiago del Estero", 
        "Tierra del Fuego", "Antártida e Islas del Atlántico Sur", "Tucumán"})

provincia = input("Ingrese una provincia para calcular su complemento: ")
conjunto_single = {provincia}

complemento = conjunto_universal.difference(conjunto_single)

print("El complemento de la provincia ingresada es el siguiente:")
print(complemento)