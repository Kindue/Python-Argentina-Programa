# Ejercicio 9
# Escriba un programa que permita que el usuario ingrese Em-
# pleadosPorHora y EmpleadosSemiExclusivos en una lista. Luego im-
# prima por pantalla el empleado por hora que gana más dinero y el
# empleado semiexclusivo que tiene sueldo más alto.


from Ejercicio7 import EmpleadoPorHora
from Ejercicio8 import EmpleadoExclusivo

listaEmpleados = []

def ingresarEmpleado(tipo):
    try:
        print("Ingrese el nombre de un nuevo empleado a agregar:")
        nombre = input()
        print("Ingrese el nombre del lugar de trabajo de este empleado:")
        lugar = input()
        if(tipo == '1'):
            print("Ingrese el precio por hora de trabajo de este empleado:")
            pph = float(input())
            print("Ingrese la cantidad de horas trabajadas por esta persona:")
            cantH = int(input())
            nuevoEmpleado = EmpleadoPorHora(nombre, lugar, pph, cantH)
        if(tipo == '2'):
            print("Ingrese el sueldo del empleado exclusivo:")
            sueldo = float(input())
            nuevoEmpleado = EmpleadoExclusivo(nombre, lugar, sueldo)
        listaEmpleados.append(nuevoEmpleado)
    except ValueError:
        print("Se ingreso una edad no valida, no se pudo agregar a esa persona!")

loop = True
while(loop):
    print("A continuacion ingrese el tipo de empleado que desee agregar:")
    print("--"*40)
    print("1 : Empleado por hora")
    print("--"*40)
    print("2 : Empleado exclusivo")
    print("--"*40)
    print("0 : Salir")
    print("--"*40)
    tipoEmpleado = input()
    if(tipoEmpleado == '1' or tipoEmpleado == '2'):
        ingresarEmpleado(tipoEmpleado)
    elif(tipoEmpleado == '0'):
        loop = False
    else:
        print("Ingreso una opcion incorrecta, vuelva a intentarlo")

mayorPPH = 0
mayorSueldo = 0

for empleado in listaEmpleados:
    if(type(empleado) == EmpleadoPorHora):
        if(empleado.dineroTotal() >= mayorPPH):
            mayorPPH = empleado.dineroTotal()
    if(type(empleado) == EmpleadoExclusivo):
        if(empleado.getSueldo() >= mayorSueldo):
            mayorSueldo = empleado.getSueldo()

print("El mayor precio por hora de los empleados ingresados es:", mayorPPH)
print("--"*40)
print("El mayor sueldo de los empleados ingresados es:", mayorSueldo)
print("--"*40)