cantidad_pa = int(input("Ingrese la cantidad de payasos vendidos: "))
cantidad_mu = int(input("Ingrese la cantidad de muñecas vendidas: "))

peso_payaso = 112 
peso_muneca = 75

peso_total = (cantidad_pa * peso_payaso) + (cantidad_mu * peso_muneca)

print("El peso total es de ", peso_total, "gramos")