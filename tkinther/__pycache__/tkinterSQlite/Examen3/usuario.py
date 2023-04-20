import threading
from tkinter import *
from tkinter import ttk
import tkinter as tk
from Constructor  import *

construrctor = Controlador()

def ejecutaIn():
    construrctor.usuario(varNom.get(),varCor.get(),varCon.get())


Ventana= Tk()
Ventana.title("FERRETERIA")
Ventana.geometry("300x300")

panel= ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

Pestaña1= ttk.Frame(panel)
Pestaña2= ttk.Frame(panel)
Pestaña3= ttk.Frame(panel)

titulo= Label(Pestaña1,text="Registro de Material", fg="purple", font=("Modern",18)).pack()

varNom= tk.StringVar()
lblNom= Label(Pestaña1, text="IDMAT: ").pack()
txtNom= Entry(Pestaña1, textvariable=varNom).pack()

varCor= tk.StringVar()
lblCor= Label(Pestaña1, text="Material: ").pack()
txtCor= Entry(Pestaña1, textvariable=varCor).pack()

varCon= tk.StringVar()
lblCon= Label(Pestaña1, text="Cantidad: ").pack()
txtCon= Entry(Pestaña1, textvariable=varCon).pack()

btnGuardar= Button(Pestaña1, text="Guardar", command=ejecutaIn)

titulo2= Label(Pestaña2,text="Actualizar Material", fg="Purple", font=("Modern",18)).pack()

varBus= tk.StringVar()
lblid= Label(Pestaña2, text="Identificador de Usuario: ").pack()
txtid= Entry(Pestaña2, textvariable=varBus).pack()
btnBus= Button(Pestaña2, text="Buscar").pack()

subBus=Label(Pestaña2,text="Encontrado", fg="green", font=("Modern",15))
textEnc= tk.Text(Pestaña2,height=5,width=52)
textEnc.pack()

#pestaña3: Consultar usuario

titulo3 = Label(Pestaña3, text="Todos los Materiales", fg="Purple", font=("Modern", 18)).pack

vartod= tk.StringVar()
lblou= Label(Pestaña3, text="Mostrar todo los materiales ", fg="Purple", font=("Modern", 18)).pack()
btntod= Button(Pestaña3, text="Buscar").pack()


tree = ttk.Treeview(Pestaña3,columns=("idmat", "material", "Cantidad"))
tree.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5)
tree.heading("#1", text="idmat")
tree.heading("#2", text="material")
tree.heading("#3", text="Cantidad")

Ventana.mainloop()
