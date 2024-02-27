#crear una clase llamada personaje
class Personaje: 
    #crear atributos del personaje
    
    #atributo del personaje
    #Declaramos el costructor para crear los objetos
    def __init__(self, esp, nom, alt):
        self.especie= esp
        self.nombre= nom
        self.altura= alt
    
    #crear los métodos del personaje
    def correr(self,estado):
        if(estado):
            print("El personaje "+ self.nombre+ " está corriendo ")
        else:
            print("El personaje "+ self.nombre+ " está muerto")
            
    #crear un segundo método del personaje el self es para llamar los atributos de la misma clase
    def lanzarGranada(self):
        # declara una variable ´para este método
        # dentro de nuestros parametros se puede tener otro parametro que no este definido pero que se puede
        # puede ocupar en el mismo método
        print(self.nombre+" Pego una granada")
    #crear un tercer método
    
#Creamos un nuevo archivo donde sólo tendremos que queremos que haga el código o sea las instancias
#En este archiv sólo tendremos las clases, atributos y los metodos