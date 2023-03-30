from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def _init_(self):
        pass
    
    # Metodo para crear conexiones
    def conexionBD(self):
        try:
            conexion= sqlite3.connect("/Users/majo0/Desktop/FPOO181/tkinterSQlite/DBUsuario.db")
            print("Conectado a la BD")
            return conexion 
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    
    #Metodo para Guardar Usuarios
    def guardarUsuario(self,Nom,Cor,Con):
        
        #1. Usamos una conexion
        Conx= self.conexionBD()
        
        #2. Validar parametros Vacios
        if(Nom == "" or Cor == "" or Con == ""):
            messagebox.showwarning("Aguas", "Formulario Incompleto")
        else:
            
            #3. Preparamos Cursor,Datos,QuerySQL
            Cursor= Conx.cursor()  
            ConH= self.encriptarCon(Con)
            Datos=(Nom,Cor,ConH)
            qrInsert= "insert into TBRegistrados(nombre,correo,contra) values(?,?,?)" 
            
            #4. Ejecutar Insert y cerramos Conexión
            Cursor.execute(qrInsert,Datos) 
            Conx.commit()
            Conx.close
            messagebox.showinfo("Éxito", "Usuario Guardado")
        
        
    # Método para encriptar Contraseñas    
    def encriptarCon(self,Con):
            ConPlana= Con
            
            
            #Preparamos con en bytes y la SAL
            ConPlana= ConPlana.encode()    #Convertimos con a bytes
            Sal= bcrypt.gensalt()
            
            #Encryptamos la contraseña
            ConHa= bcrypt.hashpw(ConPlana, Sal)
            print(ConHa)
            return ConHa
        
    #Buscar un usuario 
    def consultarUsuario (self, id):
        #1. Prepara una conexion 
        conx= self.conexionBD()
        #2 verificar si el id contiene algo
        if (id == ""):
            messagebox.showwarning("Cuidado", "Id vacio escribe algo valido")
        else:
            try:
                #preparar el cursor del query
                cursor = conx.cursor()
                selectQry = "select * from TBRegistrados where id= "+ id
                
                #4. ejecutar y guardar la consulta
                cursor.execute(selectQry)
                rsUsuario = cursor.fetchall()
                conx.close()
                
                return rsUsuario
             
            except sqlite3.OperationalError:
                print("Error consulta")        