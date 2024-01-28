nombre=input("Ingrese su nombre completo ")

nombre2=(nombre)
nombremayu=nombre2.upper()
nombremin=nombre2.lower()
nombre_div=nombre2.split()
nombre_mayusculas = ' '.join([parte[0].upper() for parte in nombre_div])



print("Tu nombre es ",nombre2)

print("Tu nombre es ",nombremayu)

print("Tu nombre es ",nombremin)

print("Tu nombre es ", nombre_mayusculas)



