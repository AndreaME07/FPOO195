from tkinter import messagebox
import sqlite3
import bcrypt

#1. Creamos la clase llamada Controlador
class Controlador:
    
    #2. creamos una función para realizar una conexion
    def conexion(self):
        try: 
            conex=sqlite3.connect("C:/Users/T480/OneDrive/Documentos/GitHub/FPOO/TkSQLite/db195.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    #3. funcion para generar la contraseña encryptada
    def encryptapass(self, cont):
        passPlana=cont
        passPlana= passPlana.encode()
        # sal es la parte de la codificación que nos ayuda a que tenga un mayor nivel de seguridad
        sal= bcrypt.gensalt()
        # hashpw nos ayuda a encriptar la contraseña, es la encryptación
        passHash= bcrypt.hashpw(passPlana, sal)
        return passHash
    #3.Creamos uno para el insert de usuario----------------------------------------------------------------------
    def insertUsuario(self,nom,corr,cont):
        conexion=self.conexion()
        if ( nom== "" or corr== "" or cont== ""):
            messagebox.showwarning("Cuidado","inputs vacios menso")
            conexion.close()
        #cursor nos ayuda a poder ejecutar el programa para poder hacer la conexion
        else: 
            try:
                cursor = conexion.cursor()
                conH= self.encryptapass(cont)
                datos=(nom, corr, conH)
                sqlInsert="Insert into tbusuarios(nombre,correo,contra) values (?,?,?)"
                cursor.execute(sqlInsert,datos)
                conexion.commit()
                conexion.close
                messagebox.showinfo("Éxito","Eso tilin!!!")
            except sqlite3.OperationalError:
                print("No se pudo ejecutar")

#--------BUSCAR UN SÓLO USUARIO-----------------------------------------------------------------------------------------------------------
    def buscarUsuario(self, nombre):
        conex = self.conexion()
        # Verifica si el nombre está vacío
        if nombre == '':
            messagebox.showwarning("Cuidado", "Inputs vacíos, por favor ingresa un nombre válido.")
            conex.close()
        else:
            try:
                cursor = conex.cursor()
                # Utiliza el nombre en la consulta SQL
                sqlSelect = "SELECT * FROM tbusuarios WHERE nombre = ?"
                cursor.execute(sqlSelect, (nombre,))
                usuario = cursor.fetchall()
                conex.close()
                return usuario
            except sqlite3.OperationalError:
                print("No se pudo ejecutar la consulta.")

                
# #--------CARGAR A LA VISTA TODOS LOS USUARIOS-----------------------------------------------------------------------------------------------------------
# Función para cargar todos los usuarios en la tabla
    def consultarUsuarios(self):
            conex = self.conexion()
            try:
                cursor = conex.cursor()
                cursor.execute("SELECT id, nombre, correo FROM tbusuarios")
                usuarios = cursor.fetchall()
                conex.close()
                return usuarios
            except sqlite3.OperationalError as error:
                print("Error al consultar usuarios:", error)

# #-----------EDITAR USUARIO--------------------------------------------------------------------------------------------------------
    def editarUsuario(self, nombre_usuario, nuevo_nombre, nuevo_correo, nueva_contra):
        try:
            conexion = sqlite3.connect("C:/Users/T480/OneDrive/Documentos/GitHub/FPOO/TkSQLite/db195.db")
            cursor = conexion.cursor()
            nueva_contra = self.encryptapass(nueva_contra)
            cursor.execute("UPDATE tbusuarios SET nombre=?, correo=?, contra=? WHERE nombre=?", (nuevo_nombre, nuevo_correo, nueva_contra, nombre_usuario))
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Usuario editado correctamente")
        except sqlite3.Error as error:
            print("Error al editar el usuario:", error)


#-----------ELIMINAR USUARIOS--------------------------------------------------------------------------------------------------------
    def eliminarUsuario(self, nombree, correoe):
        conexion = self.conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM tbusuarios WHERE nombre=? AND correo=?", (nombree, correoe,))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")

#--------------GENERAR REPORTES-------------------------------------------------------------------------------------
