import math
def area(radio):
    pi= math.pi
    return pi*radio**2
def volumen(radio, altura):
    pi=math.pi
    return pi*radio**2*altura
#pi * radio al cuadrado * altura

def area_volumen():
    area_circulo=float(input("ingrese valor del radio: "))
    area_result=area(area_circulo)
    print(f"area del circulo :{area_result}")
    
    radio_cilindro= area_circulo
    altura_cilindro=float(input("Ingrese valor de la altura: "))
    volumen1=volumen(radio_cilindro, altura_cilindro)
    print(f"Volumen del cilindro :{volumen1}")
area_volumen()