import tkinter as tk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd
from PIL import Image, ImageTk
from Funciones import *
from Encargado import Encargado
from Profesor import Profesor
from MenuEncargado import mEncargado
from MenuProfesor import mProfesor

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

    # Valido a un encargado o a un profesor segun el tipo de usuario que se quiera loguear y lo guardo como el usuario activo
    def validacion(self, tipo):
        self.master.attributes("-topmost", False)
        usuarioActivo = None
        nombre = sd.askstring("Ingresar datos", "Ingrese su nombre:")
        if(tipo == "Encargado"):
            DNI = sd.askinteger("Ingresar datos", "Ingrese su DNI:")
            if(nombre == None or DNI == None):
                mb.showerror("Error", "No se ingresaron todos los datos")
            else:
                if(validarDNI(DNI)):
                    if(validarEncargado(nombre+str(DNI))):
                        mb.showinfo("Ingreso Exitoso", "Ingreso Exitoso")
                        usuarioActivo = Encargado(nombre, DNI)
                    else:
                        mb.showerror("Error", "El encargado ingresado no existe")
                else:
                    mb.showerror("Error", "El DNI ingresado no es valido")   
        else:
            materia = sd.askstring("Ingresar datos", "Ingrese la materia que dicta:")
            curso = sd.askinteger("Ingresar datos", "Ingrese su curso:")
            division = sd.askstring("Ingresar datos", "Ingrese su division:")
            if(nombre == None or materia == None or curso == None or division == None):
                mb.showerror("Error", "No se ingresaron todos los datos")
            else:
                if(validarProfesor(nombre+materia)):
                    mb.showinfo("Ingreso Exitoso", "Ingreso Exitoso")
                    usuarioActivo = Profesor(nombre, materia, curso, division)
                else:
                    mb.showerror("Error", "El profesor ingresado no existe")
        self.master.attributes("-topmost", True)
        return usuarioActivo

    # Creo una nueva ventana para el usuario activo y oculto la ventana actual

    def menuEncargados(self):
        encargado = self.validacion("Encargado")
        if(encargado != None):
            self.master.withdraw()
            self.nuevaVentana = tk.Toplevel(self.master)
            self.app = mEncargado(self.nuevaVentana, encargado, self.master)

    def menuProfesores(self):
        profesor = self.validacion("Profesor")
        if(profesor != None):
            self.master.withdraw()
            self.nuevaVentana = tk.Toplevel(self.master)
            self.app = mProfesor(self.nuevaVentana, profesor, self.master)

# Carga los diccionarios de profesores, encargados e inscripciones desde los archivos de texto

cargarInscripciones()
try:
    cargarProfesores()
    cargarEncargados()
except FileNotFoundError:
    mb.showerror("Error", "No se encontraron los archivos 'Profesores.txt' o 'Encargados.txt'")

# Creo la ventana principal

root = tk.Tk()
root.geometry(f"300x300+{root.winfo_screenwidth()//2-150}+{root.winfo_screenheight()//2-150}")
root.resizable(False, False)
root.iconbitmap("Trabajo Final 2da parte/Archivos a entregar/imgs/sl.ico")
root.attributes("-topmost", True)
root.protocol("WM_DELETE_WINDOW", root.quit)
img = ImageTk.PhotoImage(Image.open("Trabajo Final 2da parte/Archivos a entregar/imgs/sl.png").resize((300, 300)))
label = tk.Label(root, image=img)
label.img = img
label.place(relx=0.5, rely=0.5, anchor='center')
app = MenuPrincipal(root)
root.mainloop()
