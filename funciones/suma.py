# def suma(*numeros):#da la opción de un numero de parametros indefinidos
#     resultado= sum (numeros)
#     print("suma:", resultado)
# suma(1,2,3,4)

import math

def area_cuadrado(lado):
    return lado**2 #doble asperisco es para las elevaciones
def main():
    lado_cuadrado=float(input("ingrese valor del lado: "))
    area_result=area_cuadrado(lado_cuadrado)
    print(f"area del cuadrado :{area_result}")
    
main()


