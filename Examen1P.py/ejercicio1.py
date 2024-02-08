
palabra = input("Por favor, ingresa una palabra: ")


print("La palabra descompuesta en letras con sus índices (iniciando en 1) es:")
for indice, letra in enumerate(palabra):
    print(f"{letra}: {indice + 1}")

