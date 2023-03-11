from tkinter import messagebox, Frame, Tk, Button, Label
from Caja import *
       
ventana = Tk()
ventana.title("Practica 14 Caja popular")
ventana.geometry("600x400")
        
sec1 = Frame(ventana) 
sec1.pack(expand= True, fill= "both")   
titulo = Label (sec1, text= "No.Cuenta", bg= "purple", fg= "white")
    
menu = Button(sec1, text= "SELECIONA EN EL MENU", fg= "purple", command= "")
 
ventana.mainloop()