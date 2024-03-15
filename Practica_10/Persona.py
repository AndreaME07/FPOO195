#clases, constructor, funciones
#agregar, consultar, actualizar, eliminar
class Persona:
    def __init__(self, nombre, apellido_paterno, apellido_materno, correo, contraseña):
        self.__nombre = nombre
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__correo = correo
        self.__contraseña = contraseña

    def agregar_usuario(self, lista_usuarios):
        nombre = input("Ingrese el nombre: ")
        apellido_paterno = input("Ingrese el apellido paterno: ")
        apellido_materno = input("Ingrese el apellido materno: ")
        correo = input("Ingrese el correo: ")
        contraseña = input("Ingrese la contraseña: ")
        usuario = Persona(nombre, apellido_paterno, apellido_materno, correo, contraseña)
        lista_usuarios.append(usuario)
        print("Usuario agregado correctamente.")

    def consultar_usuario(self, lista_usuarios):
        correo = input("Ingrese el correo del usuario a consultar: ")
        encontrado = False
        for usuario in lista_usuarios:
            if usuario._Persona__correo == correo:
                encontrado = True
                print("Nombre:", usuario._Persona__nombre)
                print("Apellido Paterno:", usuario._Persona__apellido_paterno)
                print("Apellido Materno:", usuario._Persona__apellido_materno)
                print("Correo:", usuario._Persona__correo)
                print("Contraseña:", usuario._Persona__contraseña)
                break
        if not encontrado:
            print("Usuario no encontrado.")

    def actualizar_usuario(self, lista_usuarios):
        correo = input("Ingrese el correo del usuario a actualizar: ")
        encontrado = False
        for usuario in lista_usuarios:
            if usuario._Persona__correo == correo:
                encontrado = True
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                nuevo_apellido_paterno = input("Ingrese el nuevo apellido paterno: ")
                nuevo_apellido_materno = input("Ingrese el nuevo apellido materno: ")
                nueva_contraseña = input("Ingrese la nueva contraseña: ")
                usuario._Persona__nombre = nuevo_nombre
                usuario._Persona__apellido_paterno = nuevo_apellido_paterno
                usuario._Persona__apellido_materno = nuevo_apellido_materno
                usuario._Persona__contraseña = nueva_contraseña
                print("Usuario actualizado correctamente.")
                break
        if not encontrado:
            print("Usuario no encontrado.")

    def eliminar_usuario(self, lista_usuarios):
        correo = input("Ingrese el correo del usuario a eliminar: ")
        encontrado = False
        for usuario in lista_usuarios:
            if usuario._Persona__correo == correo:
                encontrado = True
                lista_usuarios.remove(usuario)
                print("Usuario eliminado correctamente.")
                break
        if not encontrado:
            print("Usuario no encontrado.")
