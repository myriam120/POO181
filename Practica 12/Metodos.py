import tkinter as tk
from tkinter import messagebox, Entry

class login:
  def login(email, password):
   if email == "myriam@gmail.com" and password == "araujo1210":
          messagebox.config(text="¡Bienvenido!")
   else:
        messagebox.config(text="Verifique sus datos e intente de nuevo")