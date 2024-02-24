#crear la clase de armas con sus métodos
class Armas:
    def seleccionarArma(self,nombre):
        seleccion= int(input("Seleccionar el arma:\n 1=Rifle de asalto\n 2= Espada energia\n 3=Rifle M392\n"))
        
        if(seleccion == 1):
            print(f"Rife de asalto asignado a {nombre}")
            print(f"Municiones 7.62 * 52 mm, sin mira")
            
        if(seleccion == 2):
            print(f"Espada de energía asignada a {nombre}")
            print(f"Arma creada por los Shagheili")
            
        if(seleccion == 3):
            print(f"Rifle M392 asignada a  {nombre}")
            print(f"Municiones 7.62 * 52 mm, con mira")
            
    
    def recargarArma(self, municion):
        
        cargador= 25
        cargador= cargador + municion
        print("Arma recargada "+ str(cargador)+"%") 