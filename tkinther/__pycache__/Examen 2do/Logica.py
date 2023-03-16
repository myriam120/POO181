from tkinter import messagebox, Frame, Tk, Button, Label
import tkinter as tk
from tkinter import ttk
import random

class examn():
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
            
    examn = apellidodoma[:2] + apellidopa[:2] + nombre[:2] + Fenacimiento[:2]
    examn += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
    examn_label.config(text="Tu matricula es:" + examn)

    
    
    
    
            