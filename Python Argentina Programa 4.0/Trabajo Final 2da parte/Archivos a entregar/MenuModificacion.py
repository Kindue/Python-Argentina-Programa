import tkinter as tk
import tkinter.simpledialog as sd
import tkinter.messagebox as mb
import tkinter.scrolledtext as st
from Funciones import *

class mModificacion:
    def __init__(self, master, root, inscripcion, encargado, ventanaAnterior):
        self.master = master
        self.root = root
        self.inscripcion = inscripcion
        self.encargado = encargado
        self.ventanaAnterior = ventanaAnterior
        master.title("Modificacion de la inscripcion:"+str(inscripcion))
        master.geometry(f"900x250+{master.winfo_screenwidth()//2-450}+{master.winfo_screenheight()//2-125}")
        master.resizable(False, False)

        self.panelInscripciones = tk.Frame(master)
        self.panelInscripciones.grid(row=0, column=0, rowspan=3, sticky="nsew")
        self.panelInscripciones.config(bg="green", bd=10, relief="raised")

        self.textoInscripciones = st.ScrolledText(self.panelInscripciones, state="disabled")
        self.textoInscripciones.pack(fill="both", expand=True, side="left")
        self.textoInscripciones.config(bg="green", bd=10, relief="raised")


        self.panelBotones = tk.Frame(master)
        self.panelBotones.grid(row=0, column=1, rowspan=6, sticky="nsew")

        self.botonFechaMod = tk.Button(self.panelBotones, text="Modificar fecha", command=self.modificarFecha)
        self.botonFechaMod.grid(row=0, column=0, columnspan=2, rowspan=1, sticky="nsew")

        self.botonAlumnoMod = tk.Button(self.panelBotones, text="Modificar alumno", command=self.modificarAlumno)
        self.botonAlumnoMod.grid(row=1, column=0, columnspan=2, rowspan=1, sticky="nsew")

        self.botonMateriaMod = tk.Button(self.panelBotones, text="Modificar materia", command=self.modificarMateria)
        self.botonMateriaMod.grid(row=2, column=0, columnspan=2, rowspan=1, sticky="nsew")

        self.botonProfMod = tk.Button(self.panelBotones, text="Modificar profesor", command=self.modificarProfesor)
        self.botonProfMod.grid(row=3, column=0, columnspan=2, rowspan=1, sticky="nsew")

        self.botonCursoMod = tk.Button(self.panelBotones, text="Modificar curso", command=self.modificarCurso)
        self.botonCursoMod.grid(row=4, column=0, columnspan=2, rowspan=1, sticky="nsew")

        self.botonDivMod = tk.Button(self.panelBotones, text="Modificar division", command=self.modificarDivision)
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
                actTXTCargarDic()
                self.inscripcion = dicInscripciones[nuevaFecha+self.inscripcion.getAlumno()+self.inscripcion.getMateria()]
                self.actualizarPanelInscripciones()
            else:
                mb.showerror("Error", "La fecha ingresada no es valida")
        else:
            mb.showerror("Error", "No se ingreso una fecha")
    
    def modificarAlumno(self):
        nuevoAlumno = sd.askstring("Ingresar datos", "Ingrese el nuevo nombre del alumno:")
        if(nuevoAlumno != None):
            self.encargado.modificarAlumno(self.inscripcion, nuevoAlumno)
            actTXTCargarDic()
            self.inscripcion = dicInscripciones[self.inscripcion.getFecha()+nuevoAlumno+self.inscripcion.getMateria()]
            self.actualizarPanelInscripciones()
        else:
            mb.showerror("Error", "No se ingreso un nombre")

    def modificarMateria(self):
        nuevaMateria = sd.askstring("Ingresar datos", "Ingrese la nueva materia:")
        if(nuevaMateria != None):
            self.encargado.modificarMateria(self.inscripcion, nuevaMateria)
            actTXTCargarDic()
            self.inscripcion = dicInscripciones[self.inscripcion.getFecha()+self.inscripcion.getAlumno()+nuevaMateria]
            self.actualizarPanelInscripciones()
        else:
            mb.showerror("Error", "No se ingreso una materia")

    def modificarProfesor(self):
        nuevoProfesor = sd.askstring("Ingresar datos", "Ingrese el nuevo profesor:")
        if(nuevoProfesor != None):
            self.encargado.modificarProfesor(self.inscripcion, nuevoProfesor)
            actTXTCargarDic()
            self.inscripcion = dicInscripciones[self.inscripcion.getFecha()+self.inscripcion.getAlumno()+self.inscripcion.getMateria()]
            self.actualizarPanelInscripciones()
        else:
            mb.showerror("Error", "No se ingreso un profesor")

    def modificarCurso(self):
        nuevoCurso = sd.askinteger("Ingresar datos", "Ingrese el nuevo curso:")
        if(nuevoCurso != None):
            self.encargado.modificarCurso(self.inscripcion, nuevoCurso)
            actTXTCargarDic()
            self.inscripcion = dicInscripciones[self.inscripcion.getFecha()+self.inscripcion.getAlumno()+self.inscripcion.getMateria()]
            self.actualizarPanelInscripciones()
        else:
            mb.showerror("Error", "No se ingreso un curso")
    
    def modificarDivision(self):
        nuevaDivision = sd.askstring("Ingresar datos", "Ingrese la nueva division:")
        if(nuevaDivision != None):
            self.encargado.modificarDivision(self.inscripcion, nuevaDivision)
            actTXTCargarDic()
            self.inscripcion = dicInscripciones[self.inscripcion.getFecha()+self.inscripcion.getAlumno()+self.inscripcion.getMateria()]
            self.actualizarPanelInscripciones()
        else:
            mb.showerror("Error", "No se ingreso una division")

    def cerrarVentana(self):
        self.master.destroy()
        self.root.deiconify()
        self.ventanaAnterior.actualizarPanelInscripciones()