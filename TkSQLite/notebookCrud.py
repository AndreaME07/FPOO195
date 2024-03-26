from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *

# Crear un objeto para jalar todo lo de la clase de controlador
objControlador=Controlador()

#función para ejecutar un boton y se guarde los datos en los inputs
def ejecutaInsert():
    objControlador.insertUsuario(var1.get(),var2.get(),var3.get())
#hacer la función para buscar el usuario que nos va a regresar algo más
def busUsuario():
    usuarioBD= objControlador.buscarUsuario(varBus.get())
    if usuarioBD == []:
        messagebox.showwarning("Nada", "Id no existe en BD")
    else:
        usuarioTex.delete(1.0,END)
        for i in usuarioBD:
            usuarioTex.insert(END,f"ID:{i[0]}\nNombre: {i[1]}\nCorreo: {i[2]}\n")
        print(usuarioBD)

# def consultarUsuarios():
#     objControlador.consultarUsuarios(var1.get(), var2.get())
# def editarUsuario():
#     objControlador.editarUsuario(var1.get(), var2.get(), var3.get())
# def eliminarUsuario():
#     objControlador.eliminarUsuario(var1.get(), var2.get())

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

#---------------------------2DA PARTE------------------------------------------------------------------------------

#6. Pestaña 2: Buscar Usuario
Label(pestana2, text="Buscar usuario ", fg="#9617C6", font=("Times New Roman", 18)).pack()


varBus= tk.StringVar()
Label(pestana2, text="Id: ",  fg="#1769F8").pack()
Entry(pestana2,  textvariable=varBus).pack()

#botón para generar el usuario y salgan los datos
Button(pestana2,text="Buscar usuario", command=busUsuario).pack()

Label(pestana2, text="Usuario encontrado", fg="#9617C6", font=("Times New Roman", 18)).pack()
usuarioTex= tk.Text(pestana2,height=5,width=52)
usuarioTex.pack()
"""el tk es para mandar llamar el text, caja de texto que nos ayudan a escribir más texto, pero es mejor usar otra 
para que se cumpla la función de tabla"""






#-------------------------------------------------------------------------------------------------------------------
# Label(pestana2, text="Buscar usuario", fg="#9617C6", font=("Times New Roman", 18)).pack()

# var1 = tk.StringVar()
# Label(pestana2, text="Nombre: ", fg="#1769F8").pack()
# Entry(pestana2, textvariable=var1).pack() 

# var2 = tk.StringVar()
# Label(pestana2, text="Correo: ", fg="#1769F8").pack()
# Entry(pestana2, textvariable=var2).pack()

# Button(pestana2, text="Buscar", command=buscarUsuario).pack()

# #-------------------------------------------------------------------------------------------------------------------
# Label(pestana3, text="Consultar usuario", fg="#9617C6", font=("Times New Roman", 18)).pack()

# Button(pestana3, text="Consultar", command=consultarUsuarios).pack()

# #-------------------------------------------------------------------------------------------------------------------
# Label(pestana4, text="Editar usuario", fg="#9617C6", font=("Times New Roman", 18)).pack()

# var1 = tk.StringVar()
# Label(pestana4, text="Nombre: ", fg="#1769F8").pack()
# Entry(pestana4, textvariable=var1).pack()

# var2 = tk.StringVar()
# Label(pestana4, text="Correo: ", fg="#1769F8").pack()
# Entry(pestana4, textvariable=var2).pack()

# var3 = tk.StringVar()
# Label(pestana4, text="Nueva Contraseña: ", fg="#1769F8").pack()
# Entry(pestana4, textvariable=var3).pack()

# Button(pestana4, text="Editar", command=editarUsuario).pack()
# #-------------------------------------------------------------------------------------------------------------------
# Label(pestana5, text="Eliminar usuario", fg="#9617C6", font=("Times New Roman", 18)).pack()

# var1 = tk.StringVar()
# Label(pestana5, text="Nombre: ", fg="#1769F8").pack()
# Entry(pestana5, textvariable=var1).pack()

# var2 = tk.StringVar()
# Label(pestana5, text="Correo: ", fg="#1769F8").pack()
# Entry(pestana5, textvariable=var2).pack()

# Button(pestana5, text="Eliminar", command=eliminarUsuario).pack()

Ventana.mainloop()