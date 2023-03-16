import tkinter as tk
from tkinter import Tk
from Matricula import *

ventana = Tk()
ventana.title("MATRICULA")
ventana.geometry("500x200")

nombre_label = tk.Label(ventana, text="Nombre o nombres: ", fg= "#000066", bg="#ffcccc")
nombre_entry = tk.Entry(ventana)

apema_label = tk.Label(ventana, text="Apellido Paterno: ", fg= "#000066", bg="#ffcccc")
apema_entry = tk.Entry(ventana)

apepa_label = tk.Label(ventana, text="Apellido Materno: ", fg= "#000066", bg="#ffcccc")
apepa_entry = tk.Entry(ventana)

naci_label = tk.Label(ventana, text="Fecha de Nacimiento (DD/MM/AAAA): ", fg= "#000066", bg="#ffcccc")
naci_entry = tk.Entry(ventana)

car_label = tk.Label(ventana, text="Carrera: ",fg= "#000066", bg="#ffcccc")
car_entry = tk.Entry(ventana)

cur_label = tk.Label(ventana, text='Año en curso: ',fg= "#000066", bg="#ffcccc")
cur_entry = tk.Entry(ventana)

generar_button = tk.Button(ventana, text="Generar Matrícula", command= "")

matricula_label = tk.Label(ventana, text="Tu matrícula es" )
 
nombre_label.grid(row=0, column=0)
nombre_entry.grid(row=0, column=1)
apema_label.grid(row=1, column=0)
apema_entry.grid(row=1, column=1)
apepa_label.grid(row=2, column=0)
apepa_entry.grid(row=2, column=1)
naci_label.grid(row=3, column=0)
naci_entry.grid(row=3, column=1)
car_label.grid(row=4, column=0)
car_entry.grid(row=4, column=1)
cur_label.grid(row=5, column=0)
cur_entry.grid(row=5, column=1)

generar_button.grid(row=6, column=1)

ventana.mainloop()
