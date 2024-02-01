base = int(input("Ingrese la altura que desea que tenga del arbolito: "))

ramas = 1

separacion_rama = base - 1

while base > 0:
    print(" " * separacion_rama + "*" * ramas)
    base -= 1
    separacion_rama -= 1
    ramas += 2
