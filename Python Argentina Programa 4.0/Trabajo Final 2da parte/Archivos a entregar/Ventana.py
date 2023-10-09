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
        aRet = False
        respuesta = ""
        root.attributes("-topmost", False)
        nombre = sd.askstring("Ingresar datos", "Ingrese su nombre:")
        if(tipo == "Encargado"):
            DNI = sd.askinteger("Ingresar datos", "Ingrese su DNI:")
            if(nombre == None or DNI == None):
                respuesta = mb.showerror("Error", "No se ingresaron todos los datos")
            else:
                if(validarDNI(DNI)):
                    if(validarEncargado(nombre+str(DNI))):
                        respuesta = mb.showinfo("Ingreso Exitoso", "Ingreso Exitoso")
                        aRet = True
                        usuarioActivo = Encargado(nombre, DNI)
                    else:
                        respuesta = mb.showerror("Error", "El encargado ingresado no existe")
                else:
                    respuesta = mb.showerror("Error", "El DNI ingresado no es valido")   
        else:
            materia = sd.askstring("Ingresar datos", "Ingrese la materia que dicta:")
            curso = sd.askinteger("Ingresar datos", "Ingrese su curso:")
            division = sd.askinteger("Ingresar datos", "Ingrese su division:")
            if(nombre == None or materia == None or curso == None or division == None):
                respuesta = mb.showerror("Error", "No se ingresaron todos los datos")
            else:
                if(validarProfesor(nombre+materia)):
                    respuesta = mb.showinfo("Ingreso Exitoso", "Ingreso Exitoso")
                    aRet = True
                    usuarioActivo = Profesor(nombre, materia, curso, division)
                else:
                    respuesta = mb.showerror("Error", "El profesor ingresado no existe")
        root.attributes("-topmost", False)
        return aRet

    def menuEncargados(self):
        if(self.validacion("Encargado")):
            self.master.withdraw()
            self.nuevaVentana = tk.Toplevel(self.master)
            self.app = MenuEncargado(self.nuevaVentana)

    def menuProfesores(self):
        if(self.validacion("Profesor")):
            self.master.withdraw()
            self.nuevaVentana = tk.Toplevel(self.master)
            self.app = MenuProfesor(self.nuevaVentana)


class MenuEncargado:
    def __init__(self, master):
        self.master = master
        master.title("Menu de Encargados")
        master.geometry(f"300x300+{master.winfo_screenwidth()//2-150}+{master.winfo_screenheight()//2-150}")
        master.resizable(False, False)

        self.volverBoton = tk.Button(master, text="Crear una inscripción", command=self.crearInscripcion)
        self.volverBoton.pack()

        self.volverBoton = tk.Button(master, text="Modificar una inscripción", command=self.modificarInscripcion)
        self.volverBoton.pack()

        self.volverBoton = tk.Button(master, text="Eliminar una inscripción", command=self.eliminarInscripcion)
        self.volverBoton.pack()

        self.volverBoton = tk.Button(master, text="Volver", command=self.cerrarVentana)
        self.volverBoton.pack()

    def crearInscripcion(self):
        fecha = sd.askstring("Ingresar datos", "Ingrese la fecha de la nueva inscripcion:")
        alumno = sd.askstring("Ingresar datos", "Ingrese el nombre del alumno de la nueva inscripcion:")
        materia = sd.askstring("Ingresar datos", "Ingrese la materia de la nueva inscripcion:")
        profesor = sd.askstring("Ingresar datos", "Ingrese el profesor de la nueva inscripcion:")
        curso = sd.askinteger("Ingresar datos", "Ingrese el curso de la nueva inscripcion:")
        division = sd.askstring("Ingresar datos", "Ingrese la division de la nueva inscripcion:")
        if(validarFecha(fecha)):
            if((fecha+alumno+materia) not in dicInscripciones.keys()):
                usuarioActivo.incorporarInscripcion(fecha, alumno, materia, profesor, curso, division, dicInscripciones)
            else:
                mb.showerror("Error", "Ya existe una inscripcion con esos datos")
        else:
            mb.showerror("Error", "La fecha ingresada no es valida")

    def modificarInscripcion(self):
        self.master.withdraw()
        self.nuevaVentana = tk.Toplevel(self.master)
        self.app = MenuModificacion(self.nuevaVentana, self.master)

    def eliminarInscripcion(self):
        fecha = sd.askstring("Ingresar datos", "Ingrese la fecha de la inscripcion a eliminar:")
        alumno = sd.askstring("Ingresar datos", "Ingrese el nombre del alumno de la inscripcion a eliminar:")
        materia = sd.askstring("Ingresar datos", "Ingrese la materia de la inscripcion a eliminar:")
        if(validarFecha(fecha)):
            if((fecha+alumno+materia) in dicInscripciones.keys()):
                usuarioActivo.eliminarInscripcion(fecha, alumno, materia, dicInscripciones)
            else:
                mb.showerror("Error", "No existe una inscripcion con esos datos")
        else:
            mb.showerror("Error", "La fecha ingresada no es valida")


    def cerrarVentana(self):
        self.master.destroy()
        root.deiconify()

class MenuProfesor:
    def __init__(self, master):
        self.master = master
        master.title("Menu de Profesores")
        master.geometry(f"300x300+{master.winfo_screenwidth()//2-150}+{master.winfo_screenheight()//2-150}")
        master.resizable(False, False)

        self.volverBoton = tk.Button(master, text="Volver", command=self.cerrarVentana)
        self.volverBoton.pack()

    def cerrarVentana(self):
        self.master.destroy()
        self.main_window.deiconify()

class MenuModificacion:
    def __init__(self, master):
        self.master = master
        master.title("Modificacion de inscripciones")
        master.geometry(f"300x300+{master.winfo_screenwidth()//2-150}+{master.winfo_screenheight()//2-150}")
        master.resizable(False, False)

        self.volverBoton = tk.Button(master, text="Crear una inscripción", command=self.crearInscripcion)
        self.volverBoton.pack()

        self.volverBoton = tk.Button(master, text="Modificar una inscripción", command=self.modificarInscripcion)
        self.volverBoton.pack()

        self.volverBoton = tk.Button(master, text="Eliminar una inscripción", command=self.eliminarInscripcion)
        self.volverBoton.pack()

        self.volverBoton = tk.Button(master, text="Volver", command=self.cerrarVentana)
        self.volverBoton.pack()
        # Ingrese la inscripcion a modificar

cargarProfesores()
cargarEncargados()
usuarioActivo = None
root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)
# root.iconbitmap("icono.ico")
root.eval('tk::PlaceWindow . center')
root.config(bg="green")
root.attributes("-topmost", True)
app = MenuPrincipal(root)
root.mainloop()
