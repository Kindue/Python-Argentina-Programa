import tkinter as tk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd
from Funciones import *
from Inscripcion import Inscripcion
from Encargado import Encargado
from Profesor import Profesor

class MenuPrincipal:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Inscripciones")

        self.mEncargadosBoton = tk.Button(master, text="Menu de Encargados", command=self.menuEncargados)
        self.mEncargadosBoton.place(relx=0.5, rely=0.2, anchor="center", width=200, height=50)

        self.mProfesoresBoton = tk.Button(master, text="Menu de Profesores", command=self.menuProfesores)
        self.mProfesoresBoton.place(relx=0.5, rely=0.5, anchor="center", width=200, height=50)

        self.salirBoton = tk.Button(master, text="Salir", command=master.quit)
        self.salirBoton.place(relx=0.5, rely=0.8, anchor="center", width=200, height=50)

    def validacion(self, tipo):
        # Create a popup window that asks for user data
        aRet = False
        respuesta = ""
        root.attributes("-topmost", False)
        nombre = sd.askstring("Ingresar datos", "Ingrese su nombre:")
        if(tipo == "Encargado"):
            DNI = sd.askinteger("Ingresar datos", "Ingrese su DNI:")
            if(nombre == None or DNI == None):
                respuesta = mb.showerror("Error", "No se ingresaron todos los datos")
            else:
                if(validarEncargado(nombre+str(DNI))):
                    respuesta = mb.showinfo("Ingreso Exitoso", "Ingreso Exitoso")
                    aRet = True
                else:
                    respuesta = mb.showerror("Error", "El encargado ingresado no existe")   
        else:
            materia = sd.askstring("Ingresar datos", "Ingrese la materia que dicta:")
            curso = sd.askinteger("Ingresar datos", "Ingrese su curso:")
            division = sd.askinteger("Ingresar datos", "Ingrese su division:")
            if(nombre == None or materia == None or curso == None or division == None):
                respuesta = mb.showerror("Error", "No se ingresaron todos los datos")
            else:
                if(validarProfesor(nombre+materia+str(curso)+str(division))):
                    respuesta = mb.showinfo("Ingreso Exitoso", "Ingreso Exitoso")
                    aRet = True
                else:
                    respuesta = mb.showerror("Error", "El profesor ingresado no existe")
        root.attributes("-topmost", False)
        return aRet

    def menuEncargados(self):
        if(self.validacion("Encargado")):
            self.master.withdraw()
            self.nuevaVentana = tk.Toplevel(self.master)
            self.app = EncargadosWindow(self.nuevaVentana)

    def menuProfesores(self):
        if(self.validacion("Profesor")):
            self.master.withdraw()
            self.nuevaVentana = tk.Toplevel(self.master)
            self.app = ProfesoresWindow(self.nuevaVentana)

class EncargadosWindow:
    def __init__(self, master):
        self.master = master
        master.title("Menu de Encargados")
        master.geometry("300x300")
        master.resizable(False, False)
        master.eval('tk::PlaceWindow . center')

        # self.volverBoton = tk.Button(master, text="Crear una inscripción", command=self.cerrarVentana)
        # self.volverBoton.pack()

        # self.volverBoton = tk.Button(master, text="Modificar una inscripción", command=self.cerrarVentana)
        # self.volverBoton.pack()

        # self.volverBoton = tk.Button(master, text="Eliminar una inscripción", command=self.cerrarVentana)
        # self.volverBoton.pack()

        self.volverBoton = tk.Button(master, text="Volver", command=self.cerrarVentana)
        self.volverBoton.pack()

        # Add more buttons with functionality here

    def cerrarVentana(self):
        self.master.destroy()
        root.deiconify()

class ProfesoresWindow:
    def __init__(self, master):
        self.master = master
        master.title("Menu de Profesores")
        master.geometry("300x300")
        master.resizable(False, False)
        master.eval('tk::PlaceWindow . center')

        self.volverBoton = tk.Button(master, text="Volver", command=self.cerrarVentana)
        self.volverBoton.pack()

        # Add more buttons with functionality here

    def cerrarVentana(self):
        self.master.destroy()
        root.deiconify()

cargarProfesores()
cargarEncargados()
root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)
# root.iconbitmap("icono.ico")
root.eval('tk::PlaceWindow . center')
root.config(bg="green")
root.attributes("-topmost", True)
app = MenuPrincipal(root)
root.mainloop()
