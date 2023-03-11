from tkinter import messagebox, Frame, Tk, Button, Label
import string
import tkinter as tk
from tkinter import ttk

class Appli(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Panel de pestañas en Tcl/Tk")
        
        # Crear el panel de pestañas.
        self.notebook = ttk.Notebook(self)
        
        # Crear el contenido de cada una de las pestañas.
        self.web_label = ttk.Label(self.notebook,text="Aceptar")
        self.forum_label = ttk.Label(self.notebook,text="Menu")
        
        # Añadirlas al panel con su respectivo texto.
        self.notebook.add(self.web_label, text="Cuenta", padding=20)
        self.notebook.add(self.forum_label, text="Datos", padding=20)
        
        self.notebook.pack(padx=10, pady=10)
        self.pack()
        class GreetingFrame(ttk.Frame):
    
         def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
        
        self.name_entry = ttk.Entry(self)
        self.name_entry.pack()
        
        self.greet_button = ttk.Button(
            self, text="Saludar", command=self.say_hello)
        self.greet_button.pack()
        
        self.greet_label = ttk.Label(self)
        self.greet_label.pack()
    
    def say_hello(self):
        self.greet_label["text"] = \
            "¡Hola, {}!".format(self.name_entry.get())
class AboutFrame(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Visitanos en recursospython.com y "
                              "foro.recursospython.com.")
        self.label.pack()
        
        self.web_button = ttk.Button(self, text="Visitar web")
        self.web_button.pack(pady=10)
        
        self.forum_button = ttk.Button(self, text="Visitar foro")
        self.forum_button.pack()

        
main_window = tk.Tk()
app = Appli(main_window)
app.mainloop()