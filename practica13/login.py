from contraseña import *
def menu():
    contraseña = Contraseña()

    while True:
        print("\nMenú:")
        print("1. Cambiar longitud de la contraseña")
        print("2. Incluir mayúsculas en la contraseña")
        print("3. Incluir caracteres especiales en la contraseña")
        print("4. Generar contraseña")
        print("5. Salir")

        eleccion = input("Seleccione una opción: ")

        if eleccion == "1":
            longitud = int(input("Ingrese la longitud deseada de la contraseña: "))
            contraseña.establecer_longitud(longitud)
        elif eleccion == "2":
            incluir_mayusculas = input("¿Desea incluir mayúsculas en la contraseña? (s/n): ")
            contraseña.establecer_incluye_mayusculas(incluir_mayusculas.lower() == "s")
        elif eleccion == "3":
            incluir_caracteres_especiales = input("¿Desea incluir caracteres especiales en la contraseña? (s/n): ")
            contraseña.establecer_incluye_caracteres_especiales(incluir_caracteres_especiales.lower() == "s")
        elif eleccion == "4":
            contraseña_generada = contraseña.generar_contraseña()
            fortaleza = contraseña.comprobar_fortaleza(contraseña_generada)
            print("Contraseña generada:", contraseña_generada)
            print("Fortaleza de la contraseña:", fortaleza)
        elif eleccion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

menu()