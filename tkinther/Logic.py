from tkinter import Tk,messagebox
from tkinter import Label, Frame


def mostrarMensaje():
    messagebox.showinfo("Aviso"," Este mensaje es para avisar algo")
    messagebox.showerror("Error: ","Todo fallo con exito")
    email = email_entry.get()
    password = password_entry.get()
#mensaje a pantalla
    if email == "" or password == "":
        message_label.config(text="Por favor ingrese su correo y contraseña")
    elif email == valEmail and password == valPass:
       messagebox.showinfo("Es correcto", "Bienvenido")
    else:
       print(messagebox.showerror("Error: ","Ingrese la contraseña o correo correctos"))

ventana = Tk()
ventana.title("Bienvenido")
ventana.geometry("600x400")

email_label = Tk.Label(ventana, text="Correo electrónico:")
email_label.pack()

email_entry = Tk.Entry(ventana)
email_entry.pack()
valEmail= email_entry.get()
#---------------------------------
password_label = Tk.Label(ventana, text="Contraseña:")
password_label.pack()

password_entry = Tk.Entry(ventana, show="*")
password_entry.pack()
valPass= password_entry.get()
#---------------------------------
login_button = Tk.label(ventana, text="Ingresar", command=mostrarMensaje)
login_button.pack()

message_label = Tk.Label(ventana, text="")
message_label.pack()

ventana.mainloop()