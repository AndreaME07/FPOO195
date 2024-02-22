#crear una clase llamada personaje
class Personaje: 
    #crear atributos del personaje
    especie="Humano"
    nombre="John"
    altura=2.18
    
    #crear los métodos del personaje
    def correr(self,estado):
        if(estado):
            print("El personaje"+ self.nombre+ " está corriendo ")
        else:
            print("El personaje"+ self.nombre+ " está muerto")
            
    #crear un segundo método del personaje el self es para llamar los atributos de la misma clase
    def lanzarGranada(self):
        print(self.nombre+" Pego una granada")
    #crear un tercer método
    def recargarArma(self, municion):
        # declara una variable ´para este método
        # dentro de nuestros parametros se puede tener otro parametro que no este definido pero que se puede
        # puede ocupar en el mismo método
        cargardor=25
        cargador= cargador + municion
        print("Arma recargada "+ str(cargador)+"%")
        
#crear la primera instancia de la clase dle personaje
spartan= Personaje()
#ya podemos utilizar los metoos y los atributos una vez creada la instancia
print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)