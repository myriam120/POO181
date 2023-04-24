from tkinter import messagebox

class logica:
    def __init__(self, em,passw):
        self.__email=em
        self.__password=passw


    def loginVerificacion(self):
        if self.__email == "1" or self.__password == "2":
            messagebox.showerror("Error","Ingrese un corrreo y una contraseña valida")
        elif self.__email == "myri@upq.com" and self.__password == "2002":
            messagebox.showinfo("¡Bienvenido!","Acceso permitido")
        else:
            messagebox.showwarning("Error","El correo o la contraseña son incorrectos")
            