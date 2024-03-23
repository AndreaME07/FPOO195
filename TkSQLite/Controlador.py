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
            cursor = conexion.cursor()
            conH= self.encryptapass(cont)
            datos=(nom, corr, conH)
            sqlInsert="Insert into tbusuarios(nombre,correo,contra) values (?,?,?)"
            
            cursor.execute(sqlInsert,datos)
            conexion.commit()
            conexion.close
            messagebox.showinfo("Éxito","Eso tilin!!!")