"""Realiza un programa que solicite 10 números y los almacene en una lista, una vez
completada el usuario tendrá 2 opciones a elegir:
1. Imprimir lista invertida
2. Imprimir lista sin números repetidos"""
print("Ingresa los 10 numeros que quieres invertir o que no aparezcan los no. repetidos")
numeros = [] 
for i in range(10):
    numero = int(input("Ingresa un numero: "))
    numeros.append(numero) 
while True:
    print("Ingresa el numero 1 para inevrtir los numeros\n")
    print("Ingresa 2 para imprimir numeros sin repetir\n")
    opcion = int(input("Introduce tu selección:\n "))

    if opcion == 1:
        numeros.reverse() 
        print("Tu serie de numeros invertida es la siguiente:", numeros)
    elif opcion == 2:
        numeros_no= [] 
        for i in numeros:
            if i not in numeros_no: 
                numeros_no.append(i) 
        print(f"Tu serie de numeros sin los números repetidos: {numeros_no} {numeros}")
    else:    
        print("La opcion no es valida")
