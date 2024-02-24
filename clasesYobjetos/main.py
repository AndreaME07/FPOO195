#crear un nuevo archivo donde se va a utilizar los metodos y los atributos

#creamos la importancion del archivo de personaje
#el uso del asterisco es para decir que es TODO
from Personaje import *
from Armas import *

#crear la primer objeto de la clase del personaje
spartan= Personaje()
Arma= Armas()

#ya podemos utilizar los metodos y los atributos una vez creada la instancia
print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)

#Usamos los metdos del spartan
spartan.correr(False)
spartan.lanzarGranada()

#Usamos los metodos del arma
Arma.seleccionarArma(spartan.nombre)
Arma.recargarArma(65)