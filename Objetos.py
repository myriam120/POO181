
#1. importar las clases 
from Personaje import *

#2. solicitar atributo para el objeto 
print("")
print("### Solicitud de datos del Heroe ###")
espHeroe = input("Escribe el nombre de la especie: ")
nomHeroe = input("Escribe el nombre del heroe: ")
alturaHeroe = float(input("Escribe la altura del heroe: "))
cargaHeroe = int(input("Cuantas balas se regargan al heroe: "))

print("")
print("### Solicitud de datos del villano ###")
espV = input("Escribe el nombre de la especie del villano: ")
nomV = input("Escribe el nombre del villano: ")
alturaV = float(input("Escribe la altura del villano: "))
cargaV = int(input("Cuantas balas se regargan al villano: "))

#3. creamos 2 objetos 
Heroe = personaje(espHeroe, nomHeroe, alturaHeroe) 
Villano = personaje (espV, nomV, alturaV)


#4. accedera a sus atributos y metodos de cada obj
print("")
print("### Atributos y metodos del Heroe ###")
print("El personaje pertenece a la raza: "+ Heroe.expecie )
print("Se llama: "+ Heroe.nombre )
print("Mide: "+ str(Heroe.altura) + "Metros" )
print("")

print("Metodos personaje")
Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(cargaHeroe)

print("")
print("### Atributos y metodos del villano ###")
print("El personaje pertenece a la raza: "+ Villano.expecie )
print("Se llama: "+ Villano.nombre )
print("Mide: "+ str(Villano.altura) + "Metros" )
print("")

print("Metodos personaje")
Villano.correr(True)
Villano.lanzarGranada()
Villano.recargarArma(cargaV)


