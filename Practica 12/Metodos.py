import tkinter as tk
from tkinter import messagebox,Entry

class login:
    
 def mostrarMensaje(email, password):
     messagebox.askokcancel(text= "Bienvenido")
     
     if email == "myriam@gmail.com" and password == "araujo1210":
          messagebox.showerror(text="BIENVENIDO", fg= "#000099", bg= "BLACK")
     else:
        messagebox.showerror(text="Verifique sus datos e intente de nuevo")
        