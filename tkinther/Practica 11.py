
from tkinter import Tk, Frame, Button

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
botonAzul = Button(seccion1, text= "Boton azul", fg= "#003366")
botonAzul.place(x = 60,  y = 60)

botonMorado = Button(seccion2, text= "Boton morado", fg= "#660066")
botonMorado.grid(row =0 , column =0 )

botonVerde = Button(seccion2, text= "Boton verde", fg= "#003300")
botonVerde.grid(row =1, column =1)

botonNegro = Button(seccion3, text= "Boton negro", fg= "#990000")
botonNegro.pack()


#Main de ejecucion de ventana
ventana.mainloop()