
#crear una clase llamada personaje
class Personaje: 
    #crear atributos del personaje
    
    #atributo del personaje
    #Declaramos el costructor para crear los objetos
    #creamos parte del constructor con las variables en pruvado
    def __init__(self, esp, nom, alt):
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
        
    #creamos una función para el get 
    def getEspecie(self):
        return self.__especie
    def getNombre(self):
        return self.__nombre
    def getAltura(self):
        return self.__altura
    
    #creamos la función para el set
    def setEspecie(self, especie):
        self.__especie = especie
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setAltura(self, altura):
        self.__altura = altura
    
    #metodo de pensar
    def pensar(self):
        print("El personaje "+ self.__nombre+ " está pensando")
    #crear los métodos del personaje
    def correr(self,estado):
        if(estado):
            print("El personaje "+ self.__nombre+ " está corriendo ")
        else:
            print("El personaje "+ self.__nombre+ " está muerto")
            
    #crear un segundo método del personaje el self es para llamar los atributos de la misma clase
    def lanzarGranada(self):
        # declara una variable ´para este método
        # dentro de nuestros parametros se puede tener otro parametro que no este definido pero que se puede
        # puede ocupar en el mismo método
        print(self.__nombre+" Pego una granada")
    #crear un tercer método
    
#Creamos un nuevo archivo donde sólo tendremos que queremos que haga el código o sea las instancias
#En este archiv sólo tendremos las clases, atributos y los metodos

