# from tkinter import tk
# from tkinter import messagebox
import random


class Matricula:
    def __init__(self, nombre, apellido_paterno, apellido_materno, ano_nacimiento, carrera):
        self.__nombre = nombre
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__ano_nacimiento = ano_nacimiento
        self.__carrera = carrera

    def generar_matricula(self):
        primera_letra_nombre = self.__nombre[0]
        tres_primeras_letras_paterno = self.__apellido_paterno[:3]
        tres_primeras_letras_materno = self.__apellido_materno[:3]
        numeros_aleatorios = ''.join([str(random.randint(0, 9)) for _ in range(3)])
        ano_actual = 24  
        tres_primeras_letras_carrera = self.__carrera
        matricula = f"{self.__carrera}-{ano_actual}-{self.__ano_nacimiento}-{primera_letra_nombre}{tres_primeras_letras_paterno}{tres_primeras_letras_materno}{numeros_aleatorios}"

        return matricula


nombre = input("Ingrese su nombre: ")
apellido_paterno = input("Ingrese su apellido paterno: ")
apellido_materno = input("Ingrese su apellido materno: ")
ano_nacimiento = input("Ingrese su año de nacimiento: ")
carrera = input("Ingrese su carrera: ")

matricula = Matricula(nombre, apellido_paterno, apellido_materno, ano_nacimiento, carrera)
print("Matrícula generada:", matricula.generar_matricula())

    
    
    
    
    
    
    
    
    
    