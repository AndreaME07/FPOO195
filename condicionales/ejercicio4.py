dato = input("Ingrese una cadena de caracteres: ")

def palindromo(texto):
    texto = texto.replace(" ", "").lower()
    

    if texto == texto[::-1]:
        return True
    else:
        return False


if palindromo(dato):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
