import tkinter as tk
from Logic import *

class Ventana(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Practica 12: LOGIN")
        self.geometry("300x200")
        #Etiqueta de email
        self.email_label = tk.Label(text="CORREO ELECTRONICO:", fg="purple")
        self.email_label.pack()
        #Entry de email
        self.entryem = tk.Entry(self)
        self.entryem.pack()
        #Etiqueta de contraseña
        self.password_label = tk.Label(text="CONTRASEÑA:", fg="purple")
        self.password_label.pack()
        #Entry de contraseña con *
        self.password_entry = tk.Entry(show="*")
        self.password_entry.pack()
        #Boton de ingresar con la funcion de obtener los datos de los entry's, y mandarlos a la clase login
        self.button = tk.Button(self, text="ACEPTAR", command=self.on_button, fg="white", bg="black")
        self.button.pack()
        
    #Función para el botón
    def on_button(self):
        #se crea el objeto con los gets de los entry's
        verif=logica(self.entryem.get(),self.password_entry.get())
        #se mandan los parametros de los gets para la funcion loginveriicacion de la clase login.py
        verif.loginVerificacion()
ventana = Ventana()
ventana.mainloop()