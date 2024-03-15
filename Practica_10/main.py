#mostrar menu
#mostrar objetos
#mostrar resultados
from Persona import *

def main():
    lista_usuarios = []

    while True:
        print("1. Agregar usuario")
        print("2. Consultar usuario")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            usuario = Persona(
                input("Ingrese el nombre: "),
                input("Ingrese el apellido paterno: "),
                input("Ingrese el apellido materno: "),
                input("Ingrese el correo: "),
                input("Ingrese la contraseña: ")
            )
            lista_usuarios.append(usuario)
            print("Usuario agregado correctamente.")

        elif opcion == "2":
            Persona.consultar_usuario(lista_usuarios)

        elif opcion == "3":
            Persona.actualizar_usuario(lista_usuarios)

        elif opcion == "4":
            Persona.eliminar_usuario(lista_usuarios)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

main()
