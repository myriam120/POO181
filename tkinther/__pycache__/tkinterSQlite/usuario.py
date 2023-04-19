import threading
from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorDB import *   #1. Presentamos los archivos Controlador Vista
from tkinter import messagebox

#2. Creamos 1 objeto de la Clase ControladorBD
controlador= controladorBD()

#3. Función para disparar el botón
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())

#4. FUNCION PARA DISPARAR EL BOTON BUSQUEDA
def ejecutaSelectU():
    Usuario= controlador.consultarUsuario(varBus.get())
    for usu in Usuario:
      cadena= str(usu[0]) + " " + usu[1] + " " + usu[2] + " " + str(usu[3])

    if(Usuario):
      print(cadena)
    else:
        messagebox.showinfo("No encontrado","Ese usuario no existe en la base de datos")
        
def ejecutaSelectU():
    Usuario = controlador.consultarUsuario(varBus.get())
    if Usuario:
        cadena = "ID\tNombre\tCorreo\tContraseña\n"
        for usu in Usuario:
            cadena += f"{usu[0]}\t{usu[1]}\t{usu[2]}\t{usu[3]}\n"
        textEnc.delete('1.0', END)
        textEnc.insert('1.0', cadena)
    else:
        messagebox.showinfo("No encontrado","Ese usuario no existe en la base de datos")

def limpiarTreeview():
    for item in tree.get_children():
        tree.delete(item)
        
def mostrarUsuarios():
    limpiarTreeview()
    usuarios = controlador.exporUsuario()
    conx = controlador.exporUsuario
    for usu in usuarios:
        tree.insert("", "end", values=(usu[0], usu[1], usu[2], usu[3]))
        for record in tree.get_children():
            tree.delete(record)
        datos = conx()
        for i , row in enumerate(datos):
            tree.insert("", "end", text=str(i+1), values=row)
            
def actualizar ():
    t= threading.Thread(target= actualizar)
    t.start()

def eliminar(self, conexionBD, TBRegistrados):
    try:
            self.cursor.execute(f"USE {conexionBD}")
            # Se borran todos los registros de una tabla
            sql = f"DELETE FROM {TBRegistrados}"
            self.cursor.execute(sql)
            self.conector.commit()
            print("Se han borrado todos los registros ")
    except:
            print("Error al intentar borrar los registros")  
            TBRegistrados.eliminar ("id", "nombre", "correo", "contra")
  
def actualizaUsu (self, conexionBD, TBRegistrados):
        try:
          	# Se selecciona la base de datos
            self.cursor.execute(f"USE {conexionBD}")

            # Crear la instrucción de actualización
            sql = f"UPDATE {TBRegistrados} "
            # Se ejecuta la instrucción de actualización y se hace efectiva
            self.cursor.execute(sql)
            self.conector.commit()
            messagebox.askquestion("Se actualizó el registro correctamente.")
        except:
            messagebox.askyesnocancel("Ocurrió un error al intentar actualizar el registro.")
            TBRegistrados.actualizaUsu("id= '' ", "contraseña = '', correo= ''", "nombre = '';")
            

Ventana= Tk()
Ventana.title("CRUD de Usuarios")
Ventana.geometry("500x300")

panel= ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

Pestaña1= ttk.Frame(panel)
Pestaña2= ttk.Frame(panel)
Pestaña3= ttk.Frame(panel)
Pestaña4= ttk.Frame(panel)

# PESTAÑA1: FORMUALRIO DE USUARIOS

titulo= Label(Pestaña1,text="Registro de Usuarios", fg="purple", font=("Modern",18)).pack()

varNom= tk.StringVar()
lblNom= Label(Pestaña1, text="Nombre: ").pack()
txtNom= Entry(Pestaña1, textvariable=varNom).pack()

varCor= tk.StringVar()
lblCor= Label(Pestaña1, text="Correo: ").pack()
txtCor= Entry(Pestaña1, textvariable=varCor).pack()

varCon= tk.StringVar()
lblCon= Label(Pestaña1, text="Contraseña: ").pack()
txtCon= Entry(Pestaña1, textvariable=varCon).pack()

btnGuardar= Button(Pestaña1, text="Guardar Usuario",command=ejecutaInsert).pack()

# PESTAÑA2: BUSCAR USUARIO

titulo2= Label(Pestaña2,text="Buscar Usuario", fg="Purple", font=("Modern",18)).pack()

varBus= tk.StringVar()
lblid= Label(Pestaña2, text="Identificador de Usuario: ").pack()
txtid= Entry(Pestaña2, textvariable=varBus).pack()
btnBus= Button(Pestaña2, text="Buscar",command=ejecutaSelectU).pack()

subBus=Label(Pestaña2,text="Encontrado", fg="green", font=("Modern",15))
textEnc= tk.Text(Pestaña2,height=5,width=52)
textEnc.pack()

#pestaña3: Consultar usuario

titulo3 = Label(Pestaña3, text="TODOS LOS USUARIOS", fg="Purple", font=("Modern", 18)).pack

vartod= tk.StringVar()
lblou= Label(Pestaña3, text="Mostrar todo los usuarios ", fg="Purple", font=("Modern", 18)).pack()
btntod= Button(Pestaña3, text="Buscar", command= mostrarUsuarios ).pack()


tree = ttk.Treeview(Pestaña3,columns=("ID", "Nombre", "Correo", "Contraseña"))
tree.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5)
tree.heading("#1", text="ID")
tree.heading("#2", text="Nombre")
tree.heading("#3", text="Correo")
tree.heading("#4", text="Contraseña")

#Pestaña 4 actualizar y eliminar 
titulo= Label(Pestaña4,text="Actualizar ", fg="purple", font=("Modern",18)).pack()

varNom= tk.StringVar()
lblNom= Label(Pestaña4, text="Nombre: ").pack()
txtNom= Entry(Pestaña4, textvariable=varNom).pack()

varCor= tk.StringVar()
lblCor= Label(Pestaña4, text="Correo: ").pack()
txtCor= Entry(Pestaña4, textvariable=varCor).pack()

varCon= tk.StringVar()
lblCon= Label(Pestaña4, text="Contraseña: ").pack()
txtCon= Entry(Pestaña4, textvariable=varCon).pack()

btntod= Button(Pestaña4, text="Actualizar usuario", command= actualizaUsu).pack()

titulo= Label(Pestaña4,text="Eliminar ", fg="purple", font=("Modern",18)).pack()

varNom= tk.StringVar()
lblNom= Label(Pestaña4, text="ID: ").pack()
txtNom= Entry(Pestaña4, textvariable=varNom).pack()
btntod= Button(Pestaña4, text="Eliminar usuario", command= eliminar).pack()


panel.add(Pestaña1, text="Formulario Usuarios")
panel.add(Pestaña2, text="Buscar Usuarios")
panel.add(Pestaña3, text="Consultar Usuarios")
panel.add(Pestaña4, text="Actualizar Usuarios")

Ventana.mainloop()
