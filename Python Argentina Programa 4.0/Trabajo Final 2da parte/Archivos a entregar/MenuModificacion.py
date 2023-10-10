import tkinter as tk
import tkinter.simpledialog as sd
import tkinter.messagebox as mb
import tkinter.scrolledtext as st
from Funciones import *

class mModificacion:
    def __init__(self, master, root, inscripcion, encargado):
        self.inscripcion = inscripcion
        self.master = master
        self.encargado = encargado
        self.root = root
        master.title("Modificacion de inscripciones")
        master.geometry(f"900x250+{master.winfo_screenwidth()//2-450}+{master.winfo_screenheight()//2-125}")
        master.resizable(False, False)

        self.panelInscripciones = tk.Frame(master)
        self.panelInscripciones.grid(row=0, column=0, rowspan=3, sticky="nsew")

        self.textoInscripciones = st.ScrolledText(self.panelInscripciones, state="disabled")
        self.textoInscripciones.pack(fill="both", expand=True, side="left")

        self.panelBotones = tk.Frame(master)
        self.panelBotones.grid(row=0, column=1, rowspan=6, sticky="nsew")

        self.botonFechaMod = tk.Button(self.panelBotones, text="Modificar fecha en la inscripcion", command=self.modificarFecha)
        self.botonFechaMod.grid(row=0, column=0, columnspan=2, rowspan=1, sticky="nsew")

        self.botonAlumnoMod = tk.Button(self.panelBotones, text="Modificar alumno en la inscripcion", command=self.modificarAlumno)
        self.botonAlumnoMod.grid(row=1, column=0, columnspan=2, rowspan=1, sticky="nsew")

        self.botonMateriaMod = tk.Button(self.panelBotones, text="Modificar materia en la inscripcion", command=self.modificarMateria)
        self.botonMateriaMod.grid(row=2, column=0, columnspan=2, rowspan=1, sticky="nsew")

        self.botonProfMod = tk.Button(self.panelBotones, text="Modificar profesor en la inscripcion", command=self.modificarProfesor)
        self.botonProfMod.grid(row=3, column=0, columnspan=2, rowspan=1, sticky="nsew")

        self.botonCursoMod = tk.Button(self.panelBotones, text="Modificar curso en la inscripcion", command=self.modificarCurso)
        self.botonCursoMod.grid(row=4, column=0, columnspan=2, rowspan=1, sticky="nsew")

        self.botonDivMod = tk.Button(self.panelBotones, text="Modificar division en la inscripcion", command=self.modificarDivision)
        self.botonDivMod.grid(row=5, column=0, columnspan=2, rowspan=1, sticky="nsew")

        self.volverBoton = tk.Button(self.panelBotones, text="Volver", command=self.cerrarVentana)
        self.volverBoton.grid(row=6, column=0, columnspan=2, rowspan=1, sticky="nsew")

    # Actualizar el panel de inscripciones con las inscripciones actuales
        self.actualizarPanelInscripciones()

    def actualizarPanelInscripciones(self):
        self.textoInscripciones.config(state="normal")
        self.textoInscripciones.delete("1.0", "end")
        for inscripcion in dicInscripciones.values():
            self.textoInscripciones.insert("end", str(inscripcion)+"\n")
        self.textoInscripciones.config(state="disabled")

    def modificarFecha(self):
        nuevaFecha = sd.askstring("Ingresar datos", "Ingrese la nueva fecha:")
        if(nuevaFecha != None):
            if(validarFecha(nuevaFecha)):
                self.encargado.modificarFecha(self.inscripcion, nuevaFecha)
                self.actualizarPanelInscripciones()
                actTXTCargarDic()
            else:
                mb.showerror("Error", "La fecha ingresada no es valida")
        else:
            mb.showerror("Error", "No se ingreso una fecha")
    
    def modificarAlumno(self):
        nuevoAlumno = sd.askstring("Ingresar datos", "Ingrese el nuevo nombre del alumno:")
        if(nuevoAlumno != None):
            self.encargado.modificarAlumno(self.inscripcion, nuevoAlumno)
            self.actualizarPanelInscripciones()
            actTXTCargarDic()
        else:
            mb.showerror("Error", "No se ingreso un nombre")

    def modificarMateria(self):
        nuevaMateria = sd.askstring("Ingresar datos", "Ingrese la nueva materia:")
        if(nuevaMateria != None):
            self.encargado.modificarMateria(self.inscripcion, nuevaMateria)
            self.actualizarPanelInscripciones()
            actTXTCargarDic()
        else:
            mb.showerror("Error", "No se ingreso una materia")

    def modificarProfesor(self):
        nuevoProfesor = sd.askstring("Ingresar datos", "Ingrese el nuevo profesor:")
        if(nuevoProfesor != None):
            self.encargado.modificarProfesor(self.inscripcion, nuevoProfesor)
            self.actualizarPanelInscripciones()
            actTXTCargarDic()
        else:
            mb.showerror("Error", "No se ingreso un profesor")

    def modificarCurso(self):
        nuevoCurso = sd.askinteger("Ingresar datos", "Ingrese el nuevo curso:")
        if(nuevoCurso != None):
            self.encargado.modificarCurso(self.inscripcion, nuevoCurso)
            self.actualizarPanelInscripciones()
            actTXTCargarDic()
        else:
            mb.showerror("Error", "No se ingreso un curso")
    
    def modificarDivision(self):
        nuevaDivision = sd.askstring("Ingresar datos", "Ingrese la nueva division:")
        if(nuevaDivision != None):
            self.encargado.modificarDivision(self.inscripcion, nuevaDivision)
            self.actualizarPanelInscripciones()
            actTXTCargarDic()
        else:
            mb.showerror("Error", "No se ingreso una division")

    def cerrarVentana(self):
        self.master.destroy()
        self.root.deiconify()