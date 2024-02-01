frase = str(input("Ingresa una frase: "))
letra1 = str(input("Ingresa la letra: "))

contador_letra =+ 0

for letra in frase:
    if letra.lower() in letra1:
        contador_letra += 1
print(f"La frase'{frase}' tiene la '{letra1}' {contador_letra} veces .")