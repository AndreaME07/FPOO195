def sumatoria(lista):
    suma = sum(lista)
    return suma

def numero_mayor(lista):
    return max(lista)

def numero_menor(lista):
    return min(lista)

def promedio(lista):
    prom = sum(lista) / len(lista)
    return prom

def moda(lista):
    frecuencias = {repetido: lista.count(repetido) for repetido in lista}#esta parte la saque de internet porque no sabía como sacar la moda en python
    moda_valor = max(frecuencias, key=frecuencias.get)
    return moda_valor

def rango(lista):
    rango_val = max(lista) - min(lista)
    return rango_val

print("---------------Ahora ingresar que cantidad de numeros tendrá la tupla---------------")
numero_lista = int(input("Ingrese el largo de la lista para convertirlo en tupla "))
numeros_lista = []
for i in range(numero_lista):
    tupla_numero = int(input(f"Numero {i+1}: "))
    numeros_lista.append(tupla_numero)
tupla = tuple(numeros_lista)

print("1----Sumatoria de los numeros----")
print("2----Número mayor de la tupla----")
print("3----Número menor de la tupla----")
print("4----Promedio de la tupla----")
print("5----Moda de la tupla----")
print("6----Rango de la tupla----")
opcion = int(input("Ingrese el numero con el cual se va a hacer la operación: "))

if opcion == 1:
    resultado = sumatoria(tupla)
    print("Sumatoria de los elementos de la tupla:", resultado)
elif opcion == 2:
    resultado = numero_mayor(tupla)
    print("Número mayor de la lista:", resultado)
elif opcion == 3:
    resultado = numero_menor(tupla)
    print("Número menor de la lista:", resultado)
elif opcion == 4:
    resultado = promedio(tupla)
    print("Promedio de los elementos de la lista:", resultado)
elif opcion == 5:
    resultado = moda(tupla)
    print("Moda de la lista:", resultado)
elif opcion == 6:
    resultado = rango(tupla)
    print("Rango de la lista:", resultado)
else:
    print("Ingrese algún numero del menú que se dijo antes")

