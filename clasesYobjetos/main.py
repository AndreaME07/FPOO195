#crear un nuevo archivo donde se va a utilizar los metodos y los atributos

#creamos la importancion del archivo de personaje
#el uso del asterisco es para decir que es TODO
from Personaje import *
from Armas import *

#solicitar datos Spartan
print("======= DATOS DEL HEROE =======")
nombreS=input("Escribe el nombre de tu Spartan ")
especieS=input("Escribe la especie de tu Spartan ")
alturaS=float(input("Escribe la altura de tu Spartan "))
print("")

#solicitar datos del Nemesis
print("======= DATOS DEL NEMESIS =======")
nombreN=input("Escribe el nombre de tu Nemesis ")
especieN=input("Escribe la especie de tu Nemesis ")
alturaN= float(input("Escribe la altura de tu Nemesis "))
print("")

#crear la primer objeto de la clase del personaje
Spartan= Personaje(especieS,nombreS,alturaS)
Nemesis= Personaje(especieN,nombreN,alturaN)
Arma= Armas()

#usamos los atributos de spartan
print("======= EL OBJETO SPARTAN CONTIENE =======")
print(Spartan.getNombre())
print(Spartan.getEspecie())
print(Spartan.getAltura())
print("")

#usamos los atributos de nemesis
print("======= EL OBJETO NEMESIS CONTIENE =======")
print(Nemesis.getNombre())
print(Nemesis.getEspecie())
print(Nemesis.getAltura())
print("")

#Usamos los metodos del spartan
print("====== METODOS DEL OBJETO SPARTAN ======")
Spartan.correr(True)
Spartan.lanzarGranada()
print("")

#Usamos los metodos del Nemesis
print("====== METODOS DEL OBJETO NEMESIS ======")
Nemesis.correr(False)
Nemesis.lanzarGranada()
print("")

#Usamos los metodos del arma
Arma.seleccionarArma(Spartan.getNombre())
Arma.recargarArma(65)

#Usamos los metodos del arma
Arma.seleccionarArma(Nemesis.getNombre())
Arma.recargarArma(65)

