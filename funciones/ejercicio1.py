def calcularIVA(precio, iva=0.21):
    iva_calculado = precio * iva
    return iva_calculado

preciocompra = float(input("Ingresa el valor de la compra: "))
iva_personal = input("Ingresa el IVA en decimal o presiona Enter para usar el iva por defecto: ")

if iva_personal.strip() != "":
    iva_personal = float(iva_personal)
    IVA = calcularIVA(preciocompra, iva_personal)
else:
    IVA = calcularIVA(preciocompra)

total_factura = preciocompra + IVA

print("El valor de la compra sin IVA es de:", preciocompra)
print("El valor de la compra con IVA es de:", total_factura)



