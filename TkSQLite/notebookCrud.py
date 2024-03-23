from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *

# Crear un objeto para jalar todo lo de la clase de controlador
objControlador=Controlador()

#función para ejecutar un boton y se guarde los datos en los inputs
def ejecutaInsert():
    objControlador.insertUsuario(var1.get(),var2.get(),var3.get())

# 1 crear una ventana
Ventana = Tk()
Ventana.title("CRUD de usuarios")
Ventana.geometry("500x300")

#2. preparar el notebook para las pestañas
panel= ttk.Notebook(Ventana)
panel.pack(fill='both', expand="yes")

#3. definir las pestañas del notebook
pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)
pestana5= ttk.Frame(panel)

#4. Agregamos las pestañas

panel.add(pestana1,text="Crear Usuario")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Editar Usuario")
panel.add(pestana5,text="Eliminar Usuario")


#5. Pestaña 1: Formulario de Insert
Label(pestana1, text="Registro Usuarios", fg="#9617C6", font=("Times New Roman", 18)).pack()

var1= tk.StringVar()
Label(pestana1, text="Nombre: ",  fg="#1769F8").pack()
Entry(pestana1,  textvariable=var1).pack()

var2=tk.StringVar()
Label(pestana1, text="Correo: ", fg="#1769F8").pack()
Entry(pestana1, textvariable=var2).pack()

var3=tk.StringVar()
Label(pestana1, text="Contraseña: ", fg="#1769F8").pack()
Entry(pestana1, textvariable=var3).pack()

#botón para generar el usuario y salgan los datos
Button(pestana1,text="Guardar usuario", command=ejecutaInsert).pack()

Ventana.mainloop()