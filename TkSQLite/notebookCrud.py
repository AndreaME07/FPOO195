from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *
from GeneradorPDF import *
import os

# Crear un objeto para jalar todo lo de la clase de controlador
objControlador=Controlador()
objPDF= GeneradorPDF()

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
#función para editar usuario---------------------------------------------------------------------------------------
def editarUsuario(self, nombre_usuario, nuevo_nombre, nuevo_correo, nueva_contra):
    if nombre_usuario == '' or nuevo_nombre == '' or nuevo_correo == '' or nueva_contra == '':
        messagebox.showwarning("Cuidado", "Todos los campos son obligatorios")
    else:
        try:
            conexion = self.conexion()
            cursor = conexion.cursor()
            nueva_contra = self.encryptapass(nueva_contra)
            # Busca el usuario por su nombre en lugar de por ID
            cursor.execute("UPDATE tbusuarios SET nombre=?, correo=?, contra=? WHERE nombre=?", (nuevo_nombre, nuevo_correo, nueva_contra, nombre_usuario))
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Usuario editado correctamente")
        except sqlite3.Error as error:
            print("Error al editar el usuario:", error)

#función para cargar todos los usuarios y no sólo uno----------------------------------------------------------------
def cargarUsuarios():
    for record in tree.get_children():
        tree.delete(record)
    usuarios = objControlador.consultarUsuarios()
    for usuario in usuarios:
        tree.insert("", "end", values=usuario)
    
#funcion para eliminar usuario--------------------------------------------------------------------------------------
def eliminarUsuario():
    objControlador.eliminarUsuario(var1.get(), var2.get())
    
#funcion para gener los pdf
def ejecutaPDF():
    if varTitulo == "":
        messagebox.showwarning("Importante", "Escribe un nombre del PDF")
    else:
        objPDF.add_page()
        objPDF.chapter_body()
        objPDF.output(varTitulo.get()+".pdf")#crea el archivo y le da el nombre al archivo
        rutaPDF = "C:/Users/T480/OneDrive/Documentos/GitHub/FPOO/TkSQLite/GeneradorPDF.py"+varTitulo.get()+".pdf"
        messagebox.showinfo("Archivo creado", "PDF disponible en carpeta")
        os.system(f"start {rutaPDF}")
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
pestana6= ttk.Frame(panel)

#4. Agregamos las pestañas

panel.add(pestana1,text="Crear Usuario")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Editar Usuario")
panel.add(pestana5,text="Eliminar Usuario")
panel.add(pestana6, text="Reporte de Usuario")


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

#---------------------------2DA PARTE BUSCAR 1 SÓLO USUARIO------------------------------------------------------------------------------

#6. Pestaña 2: Buscar Usuario
Label(pestana2, text="Buscar usuario ", fg="#9617C6", font=("Times New Roman", 18)).pack()


varBus= tk.StringVar()
Label(pestana2, text="Nombre de usuario: ",  fg="#1769F8").pack()
Entry(pestana2,  textvariable=varBus).pack()

#botón para generar el usuario y salgan los datos
Button(pestana2,text="Buscar usuario", command=busUsuario).pack()

Label(pestana2, text="Usuario encontrado", fg="#9617C6", font=("Times New Roman", 18)).pack()
usuarioTex= tk.Text(pestana2,height=5,width=52)
usuarioTex.pack()
"""el tk es para mandar llamar el text, caja de texto que nos ayudan a escribir más texto, pero es mejor usar otra 
para que se cumpla la función de tabla"""
#-------------------------------CARGAR TODOS LOS USUARIO A LA VISTA------------------------------------------------------------------

# Pestaña de Cargar a todos los Usuarios
Label(pestana3, text="Consultar Usuarios", fg="#9617C6", font=("Times New Roman", 18)).pack()

tree = ttk.Treeview(pestana3, columns=("ID", "Nombre", "Correo"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Correo", text="Correo")
#esto es para el tamaño de la tabla dentro del cajón de texto
tree.column("ID", width=50)
tree.column("Nombre", width=150)
tree.column("Correo", width=200)

tree.pack()

Button(pestana3, text="Cargar Usuarios", command=cargarUsuarios).pack()

#----------------------------Editar usuario------------------------------------------------------------------------
# Para la pestaña de editar usuario
nombreu = tk.StringVar()
Label(pestana4, text="Nombre actual de usuario: ", fg="#1769F8").pack()
Entry(pestana4, textvariable=nombreu).pack()

NuevoNombre = tk.StringVar()
Label(pestana4, text="Nuevo Nombre: ", fg="#1769F8").pack()
Entry(pestana4, textvariable=NuevoNombre).pack()

NuevoCorreo = tk.StringVar()
Label(pestana4, text="Nuevo Correo: ", fg="#1769F8").pack()
Entry(pestana4, textvariable=NuevoCorreo).pack()

NuevaContra = tk.StringVar()
Label(pestana4, text="Nueva Contraseña: ", fg="#1769F8").pack()
Entry(pestana4, textvariable=NuevaContra).pack()

Button(pestana4, text="Editar Usuario", command=editarUsuario).pack()


#-----------------------------------ELIMINAR USUARIO--------------------------------------------------------------------------------
Label(pestana5, text="Eliminar usuario", fg="#9617C6", font=("Times New Roman", 18)).pack()

eliminar1 = tk.StringVar()
Label(pestana5, text="Nombre: ", fg="#1769F8").pack()
Entry(pestana5, textvariable=eliminar1).pack()

eliminar2 = tk.StringVar()
Label(pestana5, text="Correo: ", fg="#1769F8").pack()
Entry(pestana5, textvariable=eliminar2).pack()

Button(pestana5, text="Eliminar", command=eliminarUsuario).pack()

#-----------------------------------GENERAR REPORTES----------------------------------------------------------------
Label(pestana6, text="Exportar PDF", fg="#9617C6", font=("Times New Roman", 18)).pack()

varTitulo= tk.StringVar()
Label(pestana6, text="Escribe el titulo del reporte", fg="#1769F8").pack()
Entry(pestana6, textvariable=varTitulo).pack()

Button(pestana6, text="Crear PDF", command=ejecutaPDF).pack()


Ventana.mainloop()