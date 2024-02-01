entero = int(input("Ingresa un número entero: "))
suma = 0
for i in range(1, entero+1):
    suma += i
print("La suma de todos los números del 1 al", entero, "es:", suma)