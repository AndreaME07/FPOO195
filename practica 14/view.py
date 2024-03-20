import tkinter as tk
from tkinter import messagebox
from tkinter import Tk
from caja import *

cuentas = []

def crear_interfaz():
    ventana = Tk()
    ventana.title("Gestor de Cuentas")
    ventana.configure(bg="pink")  # Configuración del color de fondo rosa

    def crear_nueva_cuenta():
        numero_cuenta = numero_nueva.get()
        titular = titular_nuevo.get()
        edad = int(edad_nuevo.get())
        saldo_inicial = float(saldo_inicial_var.get())
        nueva_cuenta = Caja(numero_cuenta, titular, edad, saldo_inicial)
        cuentas.append(nueva_cuenta)
        messagebox.showinfo("Éxito", "Cuenta creada exitosamente.")

    def mostrar_mensaje():
        numero_cuenta = numero_cuenta_var.get()
        cuenta = buscar_cuenta_por_numero(cuentas, numero_cuenta)
        if cuenta:
            mensaje = f"Titular: {cuenta.obtener_titular()}\nSaldo: {cuenta.consultar_saldo()}"
            messagebox.showinfo("Información de cuenta", mensaje)
        else:
            messagebox.showwarning("Advertencia", "No se encontró ninguna cuenta con ese número.")

    def retirar_efectivo():
        numero_cuenta = numero_cuenta_var_retiro.get()
        cantidad = float(cantidad_var.get())
        cuenta = buscar_cuenta_por_numero(cuentas, numero_cuenta)
        if cuenta:
            messagebox.showinfo("Retirar Efectivo", cuenta.retirar_efectivo(cantidad))
            mostrar_mensaje()
        else:
            messagebox.showwarning("Advertencia", "No se encontró ninguna cuenta con ese número.")

    def depositar_a_otra_cuenta():
        numero_cuenta_origen = numero_cuenta_var_deposito_origen.get()
        numero_cuenta_destino = numero_cuenta_destino_var.get()
        cantidad = float(cantidad_var_deposito.get())
        cuenta_origen = buscar_cuenta_por_numero(cuentas, numero_cuenta_origen)
        cuenta_destino = buscar_cuenta_por_numero(cuentas, numero_cuenta_destino)
        if cuenta_origen and cuenta_destino:
            messagebox.showinfo("Depositar a Otra Cuenta", cuenta_origen.depositar_a_otra_cuenta(cuenta_destino, cantidad))
            mostrar_mensaje()
        else:
            messagebox.showwarning("Advertencia", "Una de las cuentas no se encontró.")

    # Elementos para crear una nueva cuenta
    tk.Label(ventana, text="Nuevo Número de Cuenta:", bg="pink").pack()
    numero_nueva = tk.StringVar()
    tk.Entry(ventana, textvariable=numero_nueva).pack()

    tk.Label(ventana, text="Nuevo Titular:", bg="pink").pack()
    titular_nuevo = tk.StringVar()
    tk.Entry(ventana, textvariable=titular_nuevo).pack()

    tk.Label(ventana, text="Nueva Edad:", bg="pink").pack()
    edad_nuevo = tk.StringVar()
    tk.Entry(ventana, textvariable=edad_nuevo).pack()

    tk.Label(ventana, text="Saldo Inicial:", bg="pink").pack()
    saldo_inicial_var = tk.StringVar()
    tk.Entry(ventana, textvariable=saldo_inicial_var).pack()

    tk.Button(ventana, text="Crear Nueva Cuenta", command=crear_nueva_cuenta).pack()
    tk.Label(ventana, text="_____________________________________________", bg="pink").pack()

    # Elementos para consultar la cuenta
    tk.Label(ventana, text="Número de Cuenta:", bg="pink").pack()
    numero_cuenta_var = tk.StringVar()
    tk.Entry(ventana, textvariable=numero_cuenta_var).pack()
    tk.Button(ventana, text="Consultar Cuenta", command=mostrar_mensaje).pack()
    tk.Label(ventana, text="_____________________________________________", bg="pink").pack()

    # Elementos para retirar dinero
    tk.Label(ventana, text="Número de Cuenta:", bg="pink").pack()
    numero_cuenta_var_retiro = tk.StringVar()
    tk.Entry(ventana, textvariable=numero_cuenta_var_retiro).pack()

    tk.Label(ventana, text="Cantidad a Retirar:", bg="pink").pack()
    cantidad_var = tk.StringVar()
    tk.Entry(ventana, textvariable=cantidad_var).pack()

    tk.Button(ventana, text="Retirar Efectivo", command=retirar_efectivo).pack()
    tk.Label(ventana, text="_____________________________________________", bg="pink").pack()

    # Elementos para depositar en otra cuenta
    tk.Label(ventana, text="Número de Cuenta Origen:", bg="pink").pack()
    numero_cuenta_var_deposito_origen = tk.StringVar()
    tk.Entry(ventana, textvariable=numero_cuenta_var_deposito_origen).pack()

    tk.Label(ventana, text="Número de Cuenta Destino:", bg="pink").pack()
    numero_cuenta_destino_var = tk.StringVar()
    tk.Entry(ventana, textvariable=numero_cuenta_destino_var).pack()

    tk.Label(ventana, text="Cantidad a Depositar:", bg="pink").pack()
    cantidad_var_deposito = tk.StringVar()
    tk.Entry(ventana, textvariable=cantidad_var_deposito).pack()

    tk.Button(ventana, text="Depositar a Otra Cuenta", command=depositar_a_otra_cuenta).pack()

    ventana.mainloop()

crear_interfaz()
