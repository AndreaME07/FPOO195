
class Caja:
    def __init__(self, numero_cuenta, titular, edad, saldo_inicial):
        self.__numero_cuenta = numero_cuenta
        self.__titular = titular
        self.__edad = edad
        self.__saldo = saldo_inicial

    def consultar_saldo(self):
        return self.__saldo

    def ingresar_efectivo(self, cantidad):
        self.__saldo += cantidad
        return f"Se han ingresado {cantidad} pesos a la cuenta. Saldo actual: {self.__saldo}"

    def retirar_efectivo(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Se han retirado {cantidad} pesos. Saldo actual: {self.__saldo}"
        else:
            return "Dinero insuficiente. El retiro no se puede hacer"

    def depositar_a_otra_cuenta(self, otra_cuenta, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            otra_cuenta.ingresar_efectivo(cantidad)
            return f"Se han depositado {cantidad} pesos a la cuenta {otra_cuenta.obtener_numero_cuenta()}"
        else:
            return "Dinero insuficiente. El depósito no se puede hacer"

    def obtener_numero_cuenta(self):
        return self.__numero_cuenta

    def obtener_titular(self):
        return self.__titular

    def obtener_edad(self):
        return self.__edad


def crear_cuenta():
    numero_cuenta = input("Ingrese el número de cuenta: ")
    titular = input("Ingrese el nombre del titular: ")
    edad = int(input("Ingrese la edad del titular: "))
    saldo_inicial = float(input("Ingrese el saldo inicial: "))
    return Caja(numero_cuenta, titular, edad, saldo_inicial)


def buscar_cuenta_por_numero(cuentas, numero_cuenta):
    for cuenta in cuentas:
        if cuenta.obtener_numero_cuenta() == numero_cuenta:
            return cuenta
    return None


def buscar_cuenta_por_titular(cuentas, titular):
    cuentas_encontradas = []
    for cuenta in cuentas:
        if cuenta.obtener_titular().lower() == titular.lower():
            cuentas_encontradas.append(cuenta)
    return cuentas_encontradas


def main():
    cuentas = []

    while True:
        print("\n1. Crear nueva cuenta")
        print("2. Seleccionar cuenta existente")
        print("3. Buscar cuenta por número")
        print("4. Buscar cuentas por titular")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            nueva_cuenta = crear_cuenta()
            cuentas.append(nueva_cuenta)
            print("Cuenta creada exitosamente.")
        elif opcion == "2":
            if not cuentas:
                print("No hay cuentas existentes. Por favor, cree una nueva cuenta.")
            else:
                print("Cuentas existentes:")
                for i, cuenta in enumerate(cuentas):
                    print(f"{i+1}. {cuenta.obtener_numero_cuenta()} - {cuenta.obtener_titular()}")
                seleccion = int(input("Seleccione una cuenta: ")) - 1
                cuenta_seleccionada = cuentas[seleccion]
                while True:
                    print("\n1. Consultar saldo")
                    print("2. Ingresar efectivo")
                    print("3. Retirar efectivo")
                    print("4. Depositar a otra cuenta")
                    print("5. Volver al menú principal")

                    opcion_cuenta = input("\nSeleccione una opción: ")

                    if opcion_cuenta == "1":
                        print("Saldo actual:", cuenta_seleccionada.consultar_saldo())
                    elif opcion_cuenta == "2":
                        cantidad = float(input("Ingrese la cantidad a ingresar: "))
                        print(cuenta_seleccionada.ingresar_efectivo(cantidad))
                    elif opcion_cuenta == "3":
                        cantidad = float(input("Ingrese la cantidad a retirar: "))
                        print(cuenta_seleccionada.retirar_efectivo(cantidad))
                    elif opcion_cuenta == "4":
                        numero_cuenta_destino = input("Ingrese el número de cuenta de destino: ")
                        cantidad = float(input("Ingrese la cantidad a depositar: "))
                        otra_cuenta = buscar_cuenta_por_numero(cuentas, numero_cuenta_destino)
                        if otra_cuenta:
                            print(cuenta_seleccionada.depositar_a_otra_cuenta(otra_cuenta, cantidad))
                        else:
                            print("La cuenta de destino no existe.")
                    elif opcion_cuenta == "5":
                        break
                    else:
                        print("Opción inválida. Por favor, seleccione una opción válida.")
        elif opcion == "3":
            numero_cuenta = input("Ingrese el número de cuenta a buscar: ")
            cuenta_encontrada = buscar_cuenta_por_numero(cuentas, numero_cuenta)
            if cuenta_encontrada:
                print(f"Titular: {cuenta_encontrada.obtener_titular()}, Saldo: {cuenta_encontrada.consultar_saldo()}")
            else:
                print("No se encontró ninguna cuenta con ese número.")
        elif opcion == "4":
            titular = input("Ingrese el nombre del titular a buscar: ")
            cuentas_encontradas = buscar_cuenta_por_titular(cuentas, titular)
            if cuentas_encontradas:
                print("Cuentas encontradas:")
                for cuenta in cuentas_encontradas:
                    print(f"Número de cuenta: {cuenta.obtener_numero_cuenta()}, Saldo: {cuenta.consultar_saldo()}")
            else:
                print("No se encontraron cuentas con ese titular.")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
main()
