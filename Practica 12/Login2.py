from Metodos import *
from tkinter import Tk, Button

root = tk.Tk()
root.title("Inicio de sesión")

email_label = tk.Label(root, text="CORREO ELECTRONICO", fg="purple")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

password_label = tk.Label(root, text="CONTRASEÑA", fg="purple")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()


inicie = Button(root, text="INICIE SESION", command= messagebox.askokcancel)
inicie.pack()

root.mainloop()