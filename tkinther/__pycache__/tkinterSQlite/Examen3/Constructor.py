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
            
    def usuario(self, idm, ma, ca):
        Conx = self.conexionBD()
        
        if idm == '' or ma == '' or ca == '':
            messagebox.showwarning('Aguas', 'Formulario Incompleto')
        else:
            Cursor = Conx.cursor()  
            ConH = self.encriptarCon(ma)
            Datos = (idm, ca, ma)
            qrInsert = 'INSERT INTO MatConstuccion (id, material, cantidad) VALUES (?, ?, ?)' 
            
            Cursor.execute(qrInsert, Datos) 
            Conx.commit()
            Conx.close()
            messagebox.showinfo('Éxito', 'Materiales Guardados') 
   
    def consultarMaterial (self, id):
        #1. Prepara una conexion 
        conx= self.conexionBD()
        #2 verificar si el id contiene algo
        if (id == ""):
            messagebox.showwarning("Cuidado", "Id vacio escribe algo valido")
        else:
            try:
                #preparar el cursor del query
                cursor = conx.cursor()
                selectQry = "select * from MatConstuccion where id= "+ id
                
                #4. ejecutar y guardar la consulta
                cursor.execute(selectQry)
                rsUsuario = cursor.fetchall()
                conx.close()
                
                return rsUsuario
             
            except sqlite3.OperationalError:
                print("Error consulta")   
                
    def ActualizarMaterial(self, id,ma,ca):
        #1. usamos una conexion 
        conx=self.conexionBD()
        
        #2. validar parámetros vacíos
        
        if(id=="" or ma=="" or ca==""):
            messagebox.showwarning("Campos incompletos")
            return False
        if ma not in ["Sí", "No"]:
            messagebox.showwarning("Error","El campo de disponibilidad solo admite sí o No, favor de seleccionar una opción válida")
            return False
        try:
            float(ca)
            cursor= conx.cursor()
            datosUP=(id,ma,ca)
            qrUPD="UPDATE MatConstuccion SET IDMat=?, Materail=?, Cantidad=? Where IDMat="+id
            cursor.execute(qrUPD,datosUP)           
            conx.commit()
            messagebox.showinfo("Exito","Material Actualizado")
            return True
        except ValueError:
            messagebox.showwarning("Error")
            return False