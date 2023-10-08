import tkinter as tk
import tkinter.simpledialog as sd
from Funciones import *

class MenuPrincipal:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Inscripciones")

        self.encargados_button = tk.Button(master, text="Menu de Encargados", command=self.open_encargados)
        self.encargados_button.pack()

        self.profesores_button = tk.Button(master, text="Menu de Profesores", command=self.open_profesores)
        self.profesores_button.pack()

        self.quit_button = tk.Button(master, text="Salir", command=master.quit)
        self.quit_button.pack()

    def validacion(self, tipo):
        # Create a popup window that asks for user data
        aRet = False
        nombre = sd.askstring("Ingresar datos", "Ingrese su nombre:")
        if(tipo == "Encargado"):
            DNI = sd.askinteger("Ingresar datos", "Ingrese su DNI:")
            if(validarEncargado(nombre+str(DNI))):
                sd.Dialog(self.master, "Ingreso Exitoso")
                aRet = True
        else:
            materia = sd.askstring("Ingresar datos", "Ingrese la materia que dicta:")
            curso = sd.askinteger("Ingresar datos", "Ingrese su curso:")
            division = sd.askinteger("Ingresar datos", "Ingrese su division:")
            if(validarProfesor(nombre+materia+str(curso)+str(division))):
                sd.Dialog(self.master, "Ingreso Exitoso")
                aRet = True
        return aRet

    def open_encargados(self):
        if(self.validacion("Encargado")):
            self.master.withdraw()
            self.new_window = tk.Toplevel(self.master)
            self.app = EncargadosWindow(self.new_window)
        else:
            sd.Dialog(self.master, "Ingreso Fallido")

    def open_profesores(self):
        if(self.validacion("Profesor")):
            self.master.withdraw()
            self.new_window = tk.Toplevel(self.master)
            self.app = ProfesoresWindow(self.new_window)
        else:
            sd.Dialog(self.master, "Ingreso Fallido")

class EncargadosWindow:
    def __init__(self, master):
        self.master = master
        master.title("Menu de Encargados")

        self.back_button = tk.Button(master, text="Volver", command=self.close_windows)
        self.back_button.pack()

        # Add more buttons with functionality here

    def close_windows(self):
        self.master.destroy()
        root.deiconify()

class ProfesoresWindow:
    def __init__(self, master):
        self.master = master
        master.title("Menu de Profesores")

        self.back_button = tk.Button(master, text="Volver", command=self.close_windows)
        self.back_button.pack()

        # Add more buttons with functionality here

    def close_windows(self):
        self.master.destroy()
        root.deiconify()

cargarProfesores()
cargarEncargados()
root = tk.Tk()
app = MenuPrincipal(root)
root.mainloop()
