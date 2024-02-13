def ingresar_tupla():
    #n = int(input("Ingrese la cantidad de números que desea agregar a la tupla: "))
    numeros = tuple(int(input(f"Ingrese el número {i+1}: ")))
    return numeros
        
print("Ingrese 1 para Sumatoria, 2 Numero mayor, 3 Numero menor, 4 promedio, 5 moda o 6 rango")
opcion = int(input("Ingrese lo que necesita hacer: "))
    
if opcion == 1:
    
    print(f"La sumatoria de los numeros es: {suma}")