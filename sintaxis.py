
#Practica2: Sintaxis Python

#1. Comentarios

#soy un comentario de 1 linea
''' soy un 
comentario
de varias lineas 
'''

#2. cadenas

'''print('soy una cadena')
print("soy otra cadena")

a=' mi banda es \n favorita es ' #la diagonal con la n es para los saltos
b= " es marrano "

print(a+b)
print(a,b)

#contar los caracteres
print(len(a))

#muestra la posicion del caracter dentro de una cadena
print(b[2:5]) 
print(b[:5])
print(b[2:])

print(a)

#3. Variables

x=int(5)
y=str("3")
z=float(5.3)

#print(type(x))
#print(type(y))

print(x)
print(y)
print(z)

import random
numero= random.randrange(1,15)
print(numero)

#4. Solicitud de datos

var1= input("introduce cualquier dato")

var2= str(input("introduce cadenas "))
var3= int(input("introduce solo enteros "))
var4= float(input("introduce numeros decimales "))

print(var1, var2, var3, var4)'''

#5. Booleans, operadores de comparacion y logicos

'''print(10 > 9)
print(10 == 9)
print(10 < 9)
print(10 >= 9)
print(10 != 9) #diferente de 
print(10 <= 9)'''

x= 1
print(x < 5 and x < 10)
print(x < 5 or x < 10)
print(not(x < 5 and x < 10))

#para operaciones binarias
'''x= 1
print(x < 5 & x < 10)
print(x < 5 | x < 10)
print(not(x < 5 & x < 10))'''