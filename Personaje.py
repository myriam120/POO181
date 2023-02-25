
class personaje:
    #creamos al constructor 
    def __init__(self, esp, nom, alt):
        self.__especie = esp
        self.__nombre = nom
        self.__altura = alt
    
    
    #metodos de persoaje 
    def correr (self, status):
        if (status):
            print ("El personaje " + self.__nombre + "Esta corriendo " )
        else:
            print ("El personaje " + self.__nombre + "Se detuvo " )
            
    def lanzarGranada(self):
        print("Se lanzo la granada ")
        
    def recargarArma(self, municiones):
        cargador  = 5 
        cargador = cargador + municiones 
        print("El arma tiene " + str(cargador) + "balas")   
        
    def getespecie(self):
        return self.__especie 
    def setespecie(self, esp):
        self.__especie = esp 
        
    def getnombre(self):
        return self.__nombre 
    def setnombre(self, nom):
        self.__nombre = nom 
        
    def getaltura(self):
        return self.__altura
    def setaltura(self, alt):
        self.__altura = alt    
             