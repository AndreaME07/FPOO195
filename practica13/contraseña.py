import random
import string

class Contraseña:
    def __init__(self):
        self.__longitud = 8
        self.__incluye_mayusculas = False
        self.__incluye_caracteres_especiales = False

    def establecer_longitud(self, longitud):
        if longitud < 8:
            print("La longitud mínima debe ser 8. Se mantendrá la longitud por defecto (8).")
        else:
            self.__longitud = longitud

    def establecer_incluye_mayusculas(self, incluye):
        self.__incluye_mayusculas = incluye

    def establecer_incluye_caracteres_especiales(self, incluye):
        self.__incluye_caracteres_especiales = incluye

    def generar_contraseña(self):
        caracteres = string.ascii_lowercase
        if self.__incluye_mayusculas:
            caracteres += string.ascii_uppercase
        if self.__incluye_caracteres_especiales:
            caracteres += string.punctuation

        contraseña = ''.join(random.choice(caracteres) for _ in range(self.__longitud))
        return contraseña

    def comprobar_fortaleza(self, contraseña):
        fortaleza = 0
        if len(contraseña) >= 8:
            fortaleza += 1
        if any(char.isupper() for char in contraseña):
            fortaleza += 1
        if any(char in string.punctuation for char in contraseña):
            fortaleza += 1
        return fortaleza