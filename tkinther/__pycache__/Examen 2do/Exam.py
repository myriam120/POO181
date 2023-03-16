from Exam import *
import tkinter as tk
from tkinter import messagebox, Frame, Tk, Button, Label
import random

ventana = tk.Tk()
ventana.title("Generador de Matrícula")

def nombre (self, nom):
        if (nom):
            print ("Escribe tu nombre:" + self.__nombre)
     
def apellidodoma (self, apema):
        if (apema):
            print ("Escribe tu apelldo materno:" + self.__apellidoma)
            
def apellidopa (self, apepa):
        if (apepa):
            print ("Escribe tu segundo apellido:" + self.__apellidopa)    
            
def Fenacimiento (self, naci):
        if (naci):
            print ("Escribe tu fecha de naciemiento:" + self.__Fenacimiento)
            
examn = apellidodoma[:2] + apellidopa[:2] + nombre[:2] + Fenacimiento[:2]
examn += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
examn.config(text="Tu matricula es:" + examn)
nombre_label = tk.Label(ventana, text="Nombre:")
nombre_entry = tk.Entry(ventana)

apellidopa_label = tk.Label(ventana, text="Apellido Paterno:")
apellidopa_entry = tk.Entry(ventana)

apellidoma_label = tk.Label(ventana, text="Apellido Materno:")
apellidoma_entry = tk.Entry(ventana)

Fenacimiento_label = tk.Label(ventana, text="Fecha de Nacimiento (DD/MM/AAAA):")
Fenacimiento_entry = tk.Entry(ventana)

gs_label = tk.Label(ventana, text="Tu grupo es:")
gs_entry = tk.Entry(ventana)

generar_button = tk.Button(ventana, text="Generar Matrícula", command=examn)

matricula_label = tk.Label(ventana, text="Tu matrícula aparecerá aquí")

# Posicionamiento de los widgets
nombre_label.grid(row=0, column=0)
nombre_entry.grid(row=0, column=1)

apellidopa_label.grid(row=1, column=0)
apellidopa_entry.grid(row=1, column=1)

apellidoma_label.grid(row=2, column=0)
apellidoma_entry.grid(row=2, column=1)

Fenacimiento_label.grid(row=3, column=0)
Fenacimiento_entry.grid(row=3, column=1)

gs_label.grid(row=4, column=0)
gs_entry.grid(row=4, column=1)


ventana.mainlop()