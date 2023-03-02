
from tkinter import Tk, Frame, Button, messagebox

#4. Funcion de mensajes para el boton 
def mostrarMensaje():
    messagebox.showinfo("Aviso", "Este mensaje es para informar algo")
    messagebox.showerror("Error", "Todo fallo con exito")
    print (messagebox.askokcancel("Pregunta:", "El o ella jugo con tu corazon"))
    
#5. Funcion para agregar botones
def agregarBoton():
    botonNegro.config(text="+", bg="#cc9900", fg="white")
    botonNuevo = Button(seccion3, text="Boton nuevo", fg= "#003300")
    botonNuevo.pack()   
    
#1 Instanciamos un objeto ventana 
ventana = Tk()
ventana.title("Practica 11:3 # Frames")
ventana.geometry("600x400")

#2. Definimos las secciones de la ventana 
seccion1 = Frame(ventana,bg="#ff99ff")
seccion1.pack(expand = True, fill = 'both')

seccion2 = Frame(ventana, bg= "#80ffff")
seccion2.pack(expand = True, fill = 'both')

seccion3 = Frame(ventana, bg= "#99ff99")
seccion3.pack(expand = True, fill = 'both')

#3. Botones 
botonAzul = Button(seccion1, text= "Boton azul", fg= "#003366", command= mostrarMensaje )
botonAzul.place(x = 60,  y = 60)

botonMorado = Button(seccion2, text= "Boton morado", fg= "#660066")
botonMorado.grid(row =0 , column =0 )

botonVerde = Button(seccion2, text= "Boton verde", fg= "#003300")
botonVerde.grid(row =1, column =1)

botonNegro = Button(seccion3, text= "Boton negro", fg= "#990000", command= agregarBoton)
botonNegro.pack()


#Main de ejecucion de ventana
ventana.mainloop()