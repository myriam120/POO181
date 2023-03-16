import tkinter as tk

ventana = tk.Tk()
ventana.title("Generador de Matrícula")

nombre_label = tk.Label(ventana, text="Nombre o Nombres:", fg="white", bg="purple")
nombre_entry = tk.Entry(ventana)

apellidopa_label = tk.Label(ventana, text="Apellido Paterno:", fg="white", bg="purple")
apellidopa_entry = tk.Entry(ventana)

apellidoma_label = tk.Label(ventana, text="Apellido Materno:", fg="white", bg="purple")
apellidoma_entry = tk.Entry(ventana)

Fenacimiento_label = tk.Label(ventana, text="Fecha de Nacimiento (DD/MM/AAAA):", fg="white", bg="purple")
Fenacimiento_entry = tk.Entry(ventana)

grup_label = tk.Label(ventana, text="Tu grupo es:", fg="white", bg="purple")
grup_entry = tk.Entry(ventana)

generar_button = tk.Button(ventana, text="Generar Matrícula", command= "")

matricula_label = tk.Label(ventana, text="Tu matrícula aparecerá aquí")

nombre_label.grid(row=0, column=0)
nombre_entry.grid(row=0, column=1)

apellidopa_label.grid(row=1, column=0)
apellidopa_entry.grid(row=1, column=1)

apellidoma_label.grid(row=2, column=0)
apellidoma_entry.grid(row=2, column=1)

Fenacimiento_label.grid(row=3, column=0)
Fenacimiento_entry.grid(row=3, column=1)

grup_label.grid(row=4, column=0)
grup_entry.grid(row=4, column=1)


ventana.mainloop()