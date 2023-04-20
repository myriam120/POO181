from tkinter import messagebox
import sqlite3
import bcrypt

conexion = sqlite3.connect('C:/Users/majo0/Documents/GitHub/POO181/tkinther/__pycache__/tkinterSQlite/Ferreteria.db')
import sqlite3
from tkinter import messagebox

class Controlador:
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion = sqlite3.connect('C:/Users/majo0/Documents/GitHub/POO181/tkinther/__pycache__/tkinterSQlite/Ferreteria.db')
            print('Conectado a la BD')
            return conexion 
        except sqlite3.OperationalError:
            print('No se pudo conectar')
            
    def usuario(self, Nom, Cor, Con):
        Conx = self.conexionBD()
        
        if Nom == '' or Cor == '' or Con == '':
            messagebox.showwarning('Aguas', 'Formulario Incompleto')
        else:
            Cursor = Conx.cursor()  
            ConH = self.encriptarCon(Con)
            Datos = (Nom, Cor, ConH)
            qrInsert = 'INSERT INTO TBRegistrados(nombre, correo, contra) VALUES (?, ?, ?)' 
            
            Cursor.execute(qrInsert, Datos) 
            Conx.commit()
            Conx.close()
            messagebox.showinfo('Éxito', 'Usuario Guardado') 
