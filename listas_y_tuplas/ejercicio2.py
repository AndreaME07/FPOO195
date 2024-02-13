import random #esta librería la tuve que buscar en internet

def num_repe(lista):
    contar = {}
    for numero in lista:
        if numero in contar:
            contar[numero] += 1
        else:
            contar[numero] = 1
    return contar

def eli_repe(lista):
    lista_sin_repetidos = []
    for num in lista:
        if num not in lista_sin_repetidos: #esta parte la busque en internet ya que no me salia el condicional
            lista_sin_repetidos.append(num)
    return lista_sin_repetidos

def reempla_cero(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                lista[j] = 0
    return lista

lista = [random.randint(10, 20) for _ in range(30)] #aquí tuve que guiarme con lo que decía en un foro para poder sacar los numeros randoms
print("Lista que se creó automaticamente:", lista)
print("--------------------Aquí están las opciones a escoger--------------------")
print("1----Contar número repetidos----")
print("2----Eliminar número repetidos----")
print("3----Reemplazar los repetidos con 0----")

opcion = int(input("-----Ingrese el número de la opción que necesita según mi menú-----"))

if opcion == 1:
    conteo = num_repe(lista)
    print("Sus numeros repetidos: ")
    for numero, repeticiones in conteo.items():
        print(f"Número {numero}: {repeticiones} veces")
elif opcion == 2:
    lista_sin_repetidos = eli_repe(lista)
    print("Lista sin que tenga numeros repetidos: ", lista_sin_repetidos)
elif opcion == 3:
    lista_reemplazo = reempla_cero(lista.copy())
    print("Lista que reemplazó los numeros repetedios con 0: ", lista_reemplazo)
else:
    print("Opción que no existe, hay que escojer del 1 al 3")
