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
    #3.Creamos uno para el insert de usuario
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
                print("Nose pudo ejecutar")

#--------BUSCAR UN SÓLO USUARIO-----------------------------------------------------------------------------------------------------------
    def buscarUsuario(self,id):
        conex = self.conexion()
        #crea una 
        if(id== ''):
            messagebox.showwarning("Cuidado", "inputs vacios no seas tibio")
            conex.close()
        else:
            try:
                cursor = conex.cursor()
                sqlSelect= "select * from tbusuarios where id=" +id
                cursor.execute(sqlSelect)
                usuario=cursor.fetchall()
                conex.close()
                return usuario
            except sqlite3.OperationalError:
                print("No se pudo ejecutar")
# #--------CONSULTAR LOS USUARIOS-----------------------------------------------------------------------------------------------------------
#     def consultarUsuarios(self, nom, correo):
#         conexion = self.conexion()
#         cursor = conexion.cursor()
#         cursor.execute("SELECT * FROM tbusuarios WHERE nombre=? AND correo=?", (nom, correo,))
#         usuarios = cursor.fetchall()
#         conexion.close()
#         if usuarios:
#             messagebox.showinfo("Usuarios encontrados", "\n".join([f"Nombre: {usuario[0]}, Correo: {usuario[1]}, Contraseña: {usuario[2]}" for usuario in usuarios]))
#         else:
#             messagebox.showinfo("Usuarios no encontrados", "No se encontraron usuarios con esos datos.")
# #-----------EDITAR USUARIO--------------------------------------------------------------------------------------------------------
#     def editarUsuario(self, nom, corr, cont):
#         conexion = self.conexion()
#         cursor = conexion.cursor()
#         conH = self.encryptapass(cont)
#         datos = (nom, conH, corr)  # Corregido el orden de los parámetros
#         cursor.execute("UPDATE tbusuarios SET nombre=?, contra=? WHERE correo=?", datos)  # Corregido el orden de los parámetros
#         conexion.commit()
#         conexion.close()
#         messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
# #-----------ELIMINAR USUARIOS--------------------------------------------------------------------------------------------------------
#     def eliminarUsuario(self, nom, corr):
#         conexion = self.conexion()
#         cursor = conexion.cursor()
#         cursor.execute("DELETE FROM tbusuarios WHERE nombre=? AND correo=?", (nom, corr,))
#         conexion.commit()
#         conexion.close()
#         messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")