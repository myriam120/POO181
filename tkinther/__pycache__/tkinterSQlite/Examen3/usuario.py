from tkinter import *
from tkinter import ttk
import tkinter as tk
from Constructor  import *
import threading

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

btnGuardar= Button(Pestaña1, text="Guardar", command=ejecutaIn).pack()

#2. pestaña dos 

titulo3 = Label(Pestaña2, text="TODOS LOS USUARIOS", fg="Purple", font=("Modern", 18)).pack

vartod= tk.StringVar()
lblou= Label(Pestaña2, text="Mostrar todo los usuarios ", fg="Purple", font=("Modern", 18)).pack()
btntod= Button(Pestaña2, text="Buscar", command=actualizaMa).pack()


tree = ttk.Treeview(Pestaña2,columns=("ID", "Material", "Cantidad"))
tree.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5)
tree.heading("#1", text="ID")
tree.heading("#2", text="Material")
tree.heading("#3", text="Cantidad")


panel.add(Pestaña1, text="Formulario de Materiales")
panel.add(Pestaña2, text="Buscar Materiales")
Ventana.mainloop()
