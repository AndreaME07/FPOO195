'''numero = int(input("Introduce un número entero positivo: "))
for impar in range(1, numero, 2):
    print(impar, end=", ")'''

numero=int(input("Ingresa un numero que sea entero positivo: "))   

for num in range(1,numero):
    if num % 2 != 0:
        print(num, end=", ")