import tkinter as tk
import tkinter.messagebox as mb
import tkinter.scrolledtext as st
from Funciones import *

class mProfesor:
    def __init__(self, master, profesor, root):
        self.master = master
        self.profesor = profesor
        self.root = root
        master.title("Menu de Profesores")
        master.geometry(f"900x250+{master.winfo_screenwidth()//2-450}+{master.winfo_screenheight()//2-125}")
        master.resizable(False, False)

        self.panelInscripciones = tk.Frame(master)
        self.panelInscripciones.grid(row=0, column=0, rowspan=3, sticky="nsew")

        self.textoInscripciones = st.ScrolledText(self.panelInscripciones, state="disabled")
        self.textoInscripciones.pack(fill="both", expand=True, side="left")

        self.panelBotones = tk.Frame(master)
        self.panelBotones.grid(row=0, column=1, rowspan=3, sticky="nsew")

        self.botonModNota = tk.Button(self.panelBotones, text="Modificar nota", command=self.modificarNota)
        self.botonModNota.grid(row=0, column=0, columnspan=2, rowspan=1, sticky="nsew")

        self.botonElimNota = tk.Button(self.panelBotones, text="Eliminar nota", command=self.eliminarNota)
        self.botonElimNota.grid(row=1, column=0, columnspan=2, rowspan=1, sticky="nsew")

        self.volverBoton = tk.Button(self.panelBotones, text="Volver", command=self.cerrarVentana)
        self.volverBoton.grid(row=2, column=0, columnspan=2, rowspan=1, sticky="nsew")

    # Actualizar el panel de inscripciones con las inscripciones actuales
        self.actualizarPanelInscripciones()

    def actualizarPanelInscripciones(self):
        self.textoInscripciones.config(state="normal")
        self.textoInscripciones.delete("1.0", "end")
        for inscripcion in dicInscripciones.values():
            self.textoInscripciones.insert("end", str(inscripcion)+"\n")
        self.textoInscripciones.config(state="disabled")

    def modificarNota(self):
        clave = preguntarClave()
        if(clave != None):
            if(validarInscripcion(clave)):
                if(dicInscripciones[clave].getMateria() == self.profesor.getMateria() and \
                   dicInscripciones[clave].getProfesor() == self.profesor.getNombre()):
                    nota = sd.askinteger("Ingresar datos", "Ingrese la nueva nota:")
                    if(nota != None):
                        self.profesor.modificarNota(dicInscripciones[clave], nota)
                        actTXTCargarDic()
                        self.actualizarPanelInscripciones()
                    else:
                        mb.showerror("Error", "No se ingreso una nota")
                else:
                    mb.showerror("Error", "Usted no es el profesor a cargo de la inscripcion ingresada")
            else:
                mb.showerror("Error", "No existe una inscripcion con esos datos")
        else:
            mb.showerror("Error", "No se ingreso una clave valida")

    def eliminarNota(self):
        clave = preguntarClave()
        if(clave != None):
            if(validarInscripcion(clave)):
                if(dicInscripciones[clave].getMateria() == self.profesor.getMateria() and \
                   dicInscripciones[clave].getProfesor() == self.profesor.getNombre()):
                    self.profesor.eliminarNota(dicInscripciones[clave])
                    actTXTCargarDic()
                    self.actualizarPanelInscripciones()
                else:
                    mb.showerror("Error", "Usted no es el profesor a cargo de la inscripcion ingresada")
            else:
                mb.showerror("Error", "No existe una inscripcion con esos datos")
        else:
            mb.showerror("Error", "No se ingreso una clave valida")

    def cerrarVentana(self):
        self.master.destroy()
        self.root.deiconify()