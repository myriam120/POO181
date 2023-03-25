from tkinter import messagebox
import sqlite3
import bcrypt

class controladorDB:
    
    def __init__(self):
        pass 
    
    def conexionBD (self):
        try:
            conexion = sqlite3.connect(""C:/SUsers/majo0/Desktop/FPOO181/tkinterSQlite/DBUsuario.db"")
            print ("Conectado a la BD")
            return conexion
        except sqlite3.OperationalError:
            print ("No se puede conectar")
            
    def guardarUsuario (self, nom, cor, con):
         
    #1. usamos una conexion 
        conx = self.conexionBD()
        
    #2. validar los parametros
        if(nom == "" or cor== "" or con ==""):
            messagebox.showwarning("Formulario incompleto")
        else: 
            
            #3. Preparamos el cursor, los datos y el querysql
            cursor = conx.cursor()
            conH = self.encriptarCon(con)
            datos =(nom,cor,conH)
            qrInsert = "insert into TBRegistros(nombre, correo, contra)values(?,?,?)"
            
            #4. Ejecutar la insert y corremos la conexion 
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", "Usuarido guardado")
            
     #metodos de encriptar contraseña        
    def encriptarCon(self,con):
        conPlana = con
        #preparamos con bytes y la sal
        conPlana = conPlana.encode() #convertimos con a bytes
        sal = bcrypt.gensalt()
        #encryptamos la contraseña 
        conHa =bcrypt.hashpw(conPlana, sal)
        print(conHa)
        #enviamos la contraseña encryptada
        return conHa