import tkinter as tk

# Definimos la funcion 
def login():
    email = email_entry.get()
    contraseña = password_entry.get()

    # Verificar el correo electrónico y la contraseña
    if email == "myriam@gmail.com" and contraseña == "araujo1210":
        message_label.config(text="¡Bienvenido!")

# Creamos la ventana para iniciar sesión 
root = tk.Tk()
root.title("Inicio de sesión")

# Creamos los atributos de correo y la contraseña 
email_label = tk.Label(root, text="Correo electrónico", fg= "white", bg= "black")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

password_label = tk.Label(root, text="Contraseña", fg= "white", bg="black")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Creamos el boton con el que inciaremos sesión 
login_button = tk.Button(root, text="Iniciar sesión", command=login, bg="#ff0000")
login_button.pack()

# Para el mensaje de bienvenida 
message_label = tk.Label(root, text="")
message_label.pack()

# Ejecutar la ventana de inicio de sesión
root.mainloop()



