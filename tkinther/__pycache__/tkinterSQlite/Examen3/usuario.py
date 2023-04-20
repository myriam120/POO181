from tkinter import *
from tkinter import ttk
import tkinter as tk
from Constructor  import *

constrolador = Controlador()

def ejecutaIn():
    constrolador.usuario(varID.get(),varMA.get(),varCA.get())
      
Ventana= Tk()
Ventana.title("FERRETERIA")
Ventana.geometry("300x300")

panel= ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

Pestaña1= ttk.Frame(panel)
Pestaña2= ttk.Frame(panel)

#1. Pestaña 1 
titulo= Label(Pestaña1,text="Registro de Material", fg="purple", font=("Modern",18)).pack()

varID= tk.StringVar()
lblID= Label(Pestaña1, text="IDMat: ").pack()
txtID= Entry(Pestaña1, textvariable=varID).pack()

varMA= tk.StringVar()
lblMA= Label(Pestaña1, text="Material: ").pack()
txtMA= Entry(Pestaña1, textvariable=varMA).pack()

varCA= tk.StringVar()
lblCA= Label(Pestaña1, text="Cantidad: ").pack()
txtCA= Entry(Pestaña1, textvariable=varCA).pack()

btnGuardar= Button(Pestaña1, text="Guardar", command=ejecutaIn)

#2. pestaña dos 

titulo2= Label(Pestaña2,text="Actualizar Material", fg="Purple", font=("Modern",18)).pack()

varBus= tk.StringVar()
lblid= Label(Pestaña2, text="Identificador de Material").pack()
txtid= Entry(Pestaña2, textvariable=varBus).pack()
btnBus= Button(Pestaña2, text="Buscar").pack()

subBus=Label(Pestaña2,text="Encontrado", fg="green", font=("Modern",15))
textEnc= tk.Text(Pestaña2,height=5,width=52)
textEnc.pack()

panel.add(Pestaña1, text="Formulario de Materiales")
panel.add(Pestaña2, text="Buscar Materiales")
Ventana.mainloop()
