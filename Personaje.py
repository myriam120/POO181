
class personaje:
    #creamos al constructor 
    def __init__(self, esp, nom, altura):
        self.especie = esp
        self.nombre = nom
        self.altura = altura
    
    
    #metodos de persoaje 
    def correr (self, status):
        if (status):
            print ("El personaje " + self.nombre + "Esta corriendo " )
        else:
            print ("El personaje " + self.nombre + "Se detuvo " )
            
    def lanzarGranada(self):
        print("Se lanzo la granada ")
        
    def recargarArma(self, municiones):
        cargador  = 5 
        cargador = cargador + municiones 
        print("El arma tiene " + cargador + "balas")    
             