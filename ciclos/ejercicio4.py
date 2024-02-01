numero = int(input("Introduce la altura del triángulo en un numero entero que no sea negativo: "))
for triangulo in range(1, numero+1):#el 1 es para decir en donde empieza, el numero+1 es que vaya aumentando y considere una posicion más y respeta la del usuario y el 2 es para que salte 2 en 2
    if triangulo % 2 != 0:
        for base in range(triangulo,0, -2):
            if base % 2 != 0:
                print(base, end=" ")
        print("")