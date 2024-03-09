import tkinter as tk
import random
from tkinter import messagebox

class generador:
    def __init__(self, length=8, mayuscula=False, caracterEspecial=False):
        self.__length = length
        self.__mayuscula = mayuscula
        self.__caracterEspecial = caracterEspecial

    def generadorcontrasena(self):
        variable = "abcdefghijklmnopqrstuvwxyz"
        if self.__mayuscula:
            variable += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if self.__caracterEspecial:
            variable += "!@#$%^&*()_+=-{}[]|\:;<>,.?/~"

        contrasena = "".join(random.choice(variable) for _ in range(self.__length))
        return contrasena

class generadorcontrasena:
    def __init__(self, ventana):
        self.__ventana = ventana
        self.generadorcontrasena = generador()

        self.length_label = tk.Label(ventana, text="Length:")
        self.length_label.grid(row=0, column=0, padx=5, pady=5)

        self.length_entry = tk.Entry(ventana)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)
        self.length_entry.insert(0, "8")

        self.mayusculaV = tk.IntVar()
        self.mayuscula_check = tk.Checkbutton(ventana, text="Mayuscula", variable=self.mayusculaV)
        self.mayuscula_check.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.especial_var = tk.IntVar()
        self.especial_check = tk.Checkbutton(ventana, text="caracter especial", variable=self.especial_var)
        self.especial_check.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.generar_button = tk.Button(ventana, text="generar contraseña", command=self.generadorcontrasena)
        self.generar_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.contrasena_entry = tk.Entry(ventana, width=30)
        self.contrasena_entry.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def generadorcontrasena(self):
        length = int(self.length_entry.get())
        mayuscula = bool(self.mayusculaV.get())
        caracterEspecial = bool(self.especial_var.get())

        self.generadorcontrasena = generador(length, mayuscula, caracterEspecial)
        contrasena = self.generadorcontrasena.generadorcontrasena()

        messagebox.showinfo("Contraseña lista", f"Su contraseña es:\n{contrasena}")
        self.contrasena_entry.delete(0, tk.END)
        self.contrasena_entry.insert(0, contrasena)

ventana.mainloop()
