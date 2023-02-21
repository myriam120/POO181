
#1. importar las clases 
from Personaje import *

#2. instanciar un objeto 
Heroe = personaje() 

#3. accedera a sus atributos 
print("Atributo personaje")
print("El personaje pertenece a la raza: "+ Heroe.expecie )
print("Se llama: "+ Heroe.nombre )
print("Mide: "+ str(Heroe.altura) + "Metros" )
print("")

print("Metodos personaje")
Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(68)

