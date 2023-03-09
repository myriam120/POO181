from tkinter import messagebox

class logic:

   def __init__(self):
       self.__contraseña= "myriam@gmail.com"
       self.__email = "araujo1210"
       
       def validarcontra(self, email, constra):
         if (email == "" or constra == ""):
            messagebox.showwarning("Cuidado revisa bien tus datos")
         else: 
             if(self.__email == email and self.__contraseña == constra)
             messagebox.showinfo("Bienvenido")
             
import tkinter as tk
import random
import string

class Contraseña():
    def _init_(self,master=None):
        super()._init-(master)
        self.caracteres = list(string.ascii_letters+string.punctuation)
        self.password = ''
        self.ancho = 8
        self.master = master
        self.pack()
        self.btnPassword()
        self.txtPassword()
        self.btnQuit()
        
    def btnPassword(self):
        self._btnPassword = tk.Button(self)
        self._btnPassword["text"] = "Contraseña Nueva"
        self._btnPassword["command"] = self._nuevoPassword
        self._btnPassword.pack(side="left")
       
    