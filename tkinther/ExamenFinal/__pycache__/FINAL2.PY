import tkinter as tk
from tkinter import messagebox
from FINAL import Convertidor

class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Conversor de números romanos y arábigos")
        self.root.geometry("300x200")

        self.lbl_numero = tk.Label(self.root, text="Ingrese el número:", fg="purple")
        self.lbl_numero.pack()

        self.ent_numero = tk.Entry(self.root)
        self.ent_numero.pack()

        self.btn_convertir = tk.Button(self.root, text="Convertir", command=self.convertir, fg="white", bg="black")
        self.btn_convertir.pack()

    def convertir(self):
        numero = self.ent_numero.get()
        conversion = Convertidor()

        if numero.isnumeric() and int(numero) > 0 and int(numero) <= 50:
            arabigo = int(numero)
            romano = conversion.arabigo_a_romano(arabigo)
            messagebox.showinfo("Resultado", f"El número romano es: {romano}")
        else:
            try:
                arabigo = conversion.romano_a_arabigo(numero.upper())
                if arabigo < 1 or arabigo > 50:
                    raise ValueError
                messagebox.showinfo("Resultado", f"El número arábigo es: {arabigo}")
            except ValueError:
                messagebox.showerror("Error", "Ingrese un número válido entre 1 y 50")

    def iniciar(self):
        self.root.mainloop()

interface = Interface()
interface.iniciar()  
