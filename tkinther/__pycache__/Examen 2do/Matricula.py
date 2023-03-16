import tkinter as tk
from tkinter import ttk
import random

class matri:
    def __init__(self, nom, apema, naci, cur, apepa, car) -> None:
        self.__nombre = nom 
        self.__apellidoma = apema
        self.__apellidopa = apepa
        self.__Fenacimiento = naci
        self.__Acurso = cur 
        self.__carrera = car
        
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
            
    matri = apellidodoma + apellidopa + nombre + Fenacimiento
    matri += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
    matri.config(text="Tu matricula es:" + matri)

    def mensaje ():
        messagebox.askyesno("Esta es tu matricula:")
    
    
    
    
            