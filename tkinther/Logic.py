from tkinter import messagebox
import random
import string

class logic:
    def _init_(self, dis,mayus,espe):
        self.__distancia=dis
        self.__mayusculas=mayus
        self.__espacio=espe


    def Seguridad(self,parametro):
        
        if parametro  < 8:
            messagebox.showerror("contraseña","La contraseña es muy fácil")
        elif parametro  < 12:
            messagebox.showerror("contraseña","La contraseña es buena pero falta reforzar")
        elif parametro  >= 13:
            messagebox.showerror("contraseña","La contraseña es la indicada")   
                
    def Contraseña(self,long, include_uppercase=False, include_special=False):
        chars = string.ascii_lowercase
        if include_uppercase:
            chars += string.ascii_uppercase
        if include_special:
            chars += string.punctuation
        password = ''.join(random.choice(chars) for _ in range(long))
        messagebox.showinfo("contraseña",password)