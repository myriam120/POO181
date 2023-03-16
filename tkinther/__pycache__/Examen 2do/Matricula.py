import tkinter as tk
from tkinter import Tk
from tkinter import Button, messagebox
import random

def __generara__ (self, nom, apema, naci, cur, apepa, car) -> None:
    self.__nombre = nom 
    self.__apellidoma = apema
    self.__apellidopa = apepa
    self.__Fenacimiento = naci
    self.__Acurso = cur 
    self.__carrera = car
    
    matricula = nom[:1] + apema[:2] + apepa[:2] + naci[-2:] + cur[-2:] + car[:3]
    matricula += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
    matricula.config(text="Tu matricula es:" + matricula)
        
        