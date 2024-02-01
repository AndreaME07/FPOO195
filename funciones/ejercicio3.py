def decimal_a_binario(decimal):
    return bin(decimal)

def binario_a_decimal(binario):
    return int(binario,2)

while True:
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")

    opcion = input("Seleccione una opción (1 o 2): ")

    if opcion == "1":
        numero_decimal = int(input("Ingrese el número decimal: "))
        resultado_binario = decimal_a_binario(numero_decimal)
        print(f"El número binario equivalente es: {resultado_binario}")

    elif opcion == "2":
        numero_binario = input("Ingrese el número binario: ")
        resultado_decimal = binario_a_decimal(numero_binario)
        print(f"El número decimal equivalente es: {resultado_decimal}")

    else:
        print("No hay más opciones :D")
        break