import random
import string
import tkinter as tk
from tkinter import messagebox

class Contraseña:
    def __init__(self):
        self.__longitud = 8
        self.__mayusculas = False
        self.__caracteres_especiales = False

    def establecer_longitud(self, longitud):
        if longitud < 8:
            messagebox.showwarning("Advertencia", "La longitud mínima debe ser 8. Se mantendrá la longitud por defecto (8).")
        else:
            self.__longitud = longitud

    def establecer_mayusculas(self, incluye):
        self.__mayusculas = incluye

    def establecer_incluye_caracteres_especiales(self, incluye):
        self.__caracteres_especiales = incluye

    def generar_contraseña(self):
        caracteres = string.ascii_lowercase
        if self.__mayusculas:
            caracteres += string.ascii_uppercase
        if self.__caracteres_especiales:
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

def generar_contraseña():
    contraseña_generada = contraseña_obj.generar_contraseña()
    fortaleza = contraseña_obj.comprobar_fortaleza(contraseña_generada)
    resultado.config(text=f"Contraseña generada: {contraseña_generada}\nFortaleza de la contraseña: {fortaleza}")

def cambiar_longitud():
    longitud = int(longitud_entry.get())
    contraseña_obj.establecer_longitud(longitud)

def incluir_mayusculas():
    incluir = mayusculas_var.get()
    contraseña_obj.establecer_mayusculas(incluir)

def incluir_caracteres_especiales():
    incluir = caracteres_especiales_var.get()
    contraseña_obj.establecer_incluye_caracteres_especiales(incluir)
contraseña_obj = Contraseña()

ventana = tk.Tk()
ventana.title("Generador de Contraseñas")

frame = tk.Frame(ventana, bg="#FFADF4")
frame.pack(padx=10, pady=10)

longitud = tk.Label(frame, text="Longitud de la contraseña:", bg="#FFADF4")
longitud.grid(row=0, column=0, sticky="w")

longitud_entry = tk.Entry(frame, bg="#FFADF4")
longitud_entry.grid(row=0, column=1, padx=5, pady=5)
longitud_entry.insert(0, "8")

mayusculas = tk.Label(frame, text="Incluir mayúsculas:", bg="#FFADF4")
mayusculas.grid(row=1, column=0, sticky="w")

mayusculas_var = tk.BooleanVar()
mayusculas = tk.Checkbutton(frame, variable=mayusculas_var, command=incluir_mayusculas,bg="#FFADF4")
mayusculas.grid(row=1, column=1, sticky="w")

caracteres_especiales = tk.Label(frame, text="Incluir caracteres especiales:", bg="#FFADF4")
caracteres_especiales.grid(row=2, column=0, sticky="w")

caracteres_especiales_var = tk.BooleanVar()
caracteres_especiales = tk.Checkbutton(frame, variable=caracteres_especiales_var, command=incluir_caracteres_especiales, bg="#FFADF4")
caracteres_especiales.grid(row=2, column=1, sticky="w")

btn_generar = tk.Button(frame, text="Generar Contraseña", command=generar_contraseña, bg="#FFADF4")
btn_generar.grid(row=3, columnspan=2, pady=10)

resultado = tk.Label(frame, text="", bg="#FFADF4")
resultado.grid(row=4, columnspan=2)

ventana.mainloop()