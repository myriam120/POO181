from tkinter import *
from tkinter import ttk
import tkinter as tk

ventana = Tk
ventana.title('Crude de usuarios')
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill= 'both', expand='yes')

pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)
pestaña3 = ttk.Frame(panel)
pestaña4 = ttk.Frame(panel)

#pestaña 1

titulo = Label(pestaña1, text="Registro de usuario", fg="purple", bg="white", font=("Modern",18)).pack()
varnom= tk.StringVar()
lblnom = Label(pestaña1, text= 'Nombre').pack()
txtnom = Entry(pestaña1, textvariable= varnom).pack()

varcor= tk.StringVar()
lblcor = Label(pestaña1, text= 'Nombre').pack()
txtcor = Entry(pestaña1, textvariable= varcor).pack()

varcon= tk.StringVar()
lblcon = Label(pestaña1, text= 'Nombre').pack()
txtcon = Entry(pestaña1, textvariable= varcon).pack()

btnGuardar = Button(pestaña1, text= "Guardar usuario").pack()

panel.add(pestaña1, text='Formulario de usuarios:')
panel.add(pestaña2, text='Buscar usuario:')
panel.add(pestaña3, text='Consultar usuario:')
panel.add(pestaña4, text='Actualizar usuario:')



ventana.mainloop()