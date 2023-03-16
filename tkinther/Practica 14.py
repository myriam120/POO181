from tkinter import messagebox, Frame, Tk, Button, Label
import tkinter as tk
from tkinter import ttk
class Appli():
    def __init__(self) -> None:
        self.__cuenta 
        self.__Edad
        self.__titular 
        self.__saldo
        self.__menu 
        
        self.notebook.add(self.web_label, text="Cuenta", padding=20)
        self.notebook.add(self.forum_label, text="Datos", padding=20) 
        
        self.notebook.pack(padx=10, pady=10)
        self.pack()
            
        def __init__(self, main_window):
          super().__init__(main_window)
        main_window.title("Caja popular")
        
        class GreetingFrame(ttk.Frame):
    
         def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
        
        self.name_entry = ttk.Entry(self)
        self.name_entry.pack()
        
        self.greet_button = ttk.Button(
            self, text="Aceptar", command=self.say_hello)
        self.greet_button.pack()
       
         
         
main_window = tk.Tk()
app = Appli(main_window)
app.mainloop()