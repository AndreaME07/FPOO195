import tkinter as tk
from tkinter import messagebox
from usuario import *

def generar_matricula():
    nombre = entry_nombre.get()
    apellido_paterno = entry_apellido_paterno.get()
    apellido_materno = entry_apellido_materno.get()
    ano_nacimiento = entry_ano_nacimiento.get()
    carrera = entry_carrera.get()
    ano_actual = entry_ano_actual.get()

    matricula_obj = Matricula(nombre, apellido_paterno, apellido_materno, ano_nacimiento, carrera, ano_actual)
    matricula_generada = matricula_obj.generar_matricula()
    messagebox.showinfo("Matrícula Generada", f"Matrícula generada: {matricula_generada}")

ventana = tk.Tk()
ventana.title("Generador de Matrícula")


tk.Label(ventana, text="Nombre: ").grid(row=0, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Apellido Paterno: ").grid(row=1, column=0)
entry_apellido_paterno = tk.Entry(ventana)
entry_apellido_paterno.grid(row=1, column=1)

tk.Label(ventana, text="Apellido Materno: ").grid(row=2, column=0)
entry_apellido_materno = tk.Entry(ventana)
entry_apellido_materno.grid(row=2, column=1)

tk.Label(ventana, text="Año de Nacimiento: ").grid(row=3, column=0)
entry_ano_nacimiento = tk.Entry(ventana)
entry_ano_nacimiento.grid(row=3, column=1)

tk.Label(ventana, text="Carrera: ").grid(row=4, column=0)
entry_carrera = tk.Entry(ventana)
entry_carrera.grid(row=4, column=1)

tk.Label(ventana, text="Año Actual: ").grid(row=5, column=0)
entry_ano_actual = tk.Entry(ventana)
entry_ano_actual.grid(row=5, column=1)


button_generar = tk.Button(ventana, text="Generar Matrícula", command=generar_matricula)
button_generar.grid(row=6, columnspan=2)


ventana.mainloop()
