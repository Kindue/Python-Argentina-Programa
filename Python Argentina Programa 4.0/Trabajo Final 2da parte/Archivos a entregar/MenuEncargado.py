import tkinter as tk
import tkinter.messagebox as mb
from PIL import Image, ImageTk
from Funciones import *
from MenuModificacion import mModificacion
import tkinter.scrolledtext as st



class mEncargado:
    def __init__(self, master, encargado, root):
        self.master = master
        self.encargado = encargado
        self.root = root
        master.title("Menu de Encargados")
        master.geometry(f"900x250+{master.winfo_screenwidth()//2-450}+{master.winfo_screenheight()//2-125}")
        master.resizable(False, False)
        master.iconbitmap("Trabajo Final 2da parte/Archivos a entregar/imgs/sl.ico")
        master.attributes("-topmost", True)
        master.protocol("WM_DELETE_WINDOW", master.quit)

        # Creo el panel de inscripciones para mostrar las inscripciones actuales

        self.panelInscripciones = tk.Frame(master)
        self.panelInscripciones.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.textoInscripciones = st.ScrolledText(self.panelInscripciones, state="disabled")
        self.textoInscripciones.pack(fill="both", expand=True, side="left")
        self.textoInscripciones.config(font=("Consolas", 12))

        # Creo el panel de botones para las opciones del encargado

        self.panelBotones = tk.Frame(master)
        self.panelBotones.grid(row=0, column=1, rowspan=4, sticky="nsew")

        self.botonCrearIns = tk.Button(self.panelBotones, text="Crear una inscripción", command=self.crearInscripcion)
        self.botonCrearIns.grid(row=0, column=0, columnspan=2, rowspan=1, sticky="nsew")

        self.botonModIns = tk.Button(self.panelBotones, text="Modificar una inscripción", command=self.modificarInscripcion)
        self.botonModIns.grid(row=1, column=0, columnspan=2, rowspan=1, sticky="nsew")

        self.botonElimIns = tk.Button(self.panelBotones, text="Eliminar una inscripción", command=self.eliminarInscripcion)
        self.botonElimIns.grid(row=2, column=0, columnspan=2, rowspan=1, sticky="nsew")

        self.volverBoton = tk.Button(self.panelBotones, text="Volver", command=self.cerrarVentana)
        self.volverBoton.grid(row=3, column=0, columnspan=2, rowspan=1, sticky="nsew")

        # Actualizar el panel de inscripciones con las inscripciones actuales

        self.actualizarPanelInscripciones()

    def actualizarPanelInscripciones(self):
        self.textoInscripciones.config(state="normal")
        self.textoInscripciones.delete("1.0", "end")
        for inscripcion in dicInscripciones.values():
            self.textoInscripciones.insert("end", str(inscripcion)+"\n")
        self.textoInscripciones.config(state="disabled")

    # Funciones de los botones

    def crearInscripcion(self):
        fecha, alumno, materia, profesor, curso, division = preguntarDatos()
        if(fecha != None and alumno != None and materia != None and profesor != None and curso != None and division != None):
            if(fecha+alumno+materia not in dicInscripciones.keys()):
                self.encargado.incorporarInscripcion(fecha, alumno, materia, profesor, curso, division, dicInscripciones)
                actTXTCargarDic()
                self.actualizarPanelInscripciones()
            else:
                mb.showerror("Error", "Ya existe una inscripcion con esos datos")
        else:
            mb.showerror("Error", "No se ingresaron todos los datos")

    def modificarInscripcion(self):
        clave = preguntarClave()
        if(clave != None and clave in dicInscripciones.keys()):
            if(validarInscripcion(clave)):
                self.master.withdraw()
                self.nuevaVentana = tk.Toplevel(self.master)
                self.app = mModificacion(self.nuevaVentana, self.master, dicInscripciones[clave], self.encargado, self)
            else:
                mb.showerror("Error", "No existe una inscripcion con esos datos")
        else:
            mb.showerror("Error", "No se ingreso una clave valida")

    def eliminarInscripcion(self):
        clave = preguntarClave()
        if(clave != None):
            if(validarInscripcion(clave)):
                self.encargado.eliminarInscripcion(dicInscripciones[clave], dicInscripciones)
                actTXTCargarDic()
                self.actualizarPanelInscripciones()
            else:
                mb.showerror("Error", "No existe una inscripcion con esos datos")
        else:
            mb.showerror("Error", "No se ingreso una clave valida")


    def cerrarVentana(self):
        self.master.destroy()
        self.root.deiconify()

