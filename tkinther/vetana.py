from tkinter import *
from  vetana import *
import tkinter as tk

axc = login ()

def ejecuta():
    axc.validarcontra()

ventana = Tk()
ventana.title("PRACTICA 13 ")
ventana.geometry("300x150")

seccion1 = Frame(ventana)
seccion1.pack(expand= True, fild= BOTH)

titulo = Label(seccion1, text="Pasword automatico", bg="purple", fg="white")
var1 = tk.StringVar()
lblemail = Label(seccion1, text= "Correo: ").pack
txtemail =Entry(seccion1)

var2 =tk.StringVar()
lblcontraseña = Label(seccion1, text="Contraseña: ")
txtcontraseña = Entry(seccion1)

botonacc = Button(seccion1 text="Aceptar", bg="white", fg="purple")
butonacc.pack()

ventana.mainloop()