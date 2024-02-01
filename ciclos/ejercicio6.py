print ("Escriba sus ingresos diferenciando D depósito o R retiro o enter para salir mas la cantidad a sumar")

saldo=0
ingreso=" "
while ingreso != "":
    ingreso = input("")
    for i in ingreso:
        if i in "D" :
            espacio = ingreso[1:]
            saldo+= int(espacio)
        elif i in "R":
            espacio = ingreso[1:]
            saldo-= int(espacio)
        else :
            saldo+=0
print(f"Su total de su dinero es: '{saldo}' pesos ")