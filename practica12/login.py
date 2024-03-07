from tkinter import Tk, messagebox

class Login():
    def __init__(self):
        self.title("Login")

        self.label_correo = tk.Label(self, text="Correo:")
        self.label_correo.grid(row=0, column=0, sticky="e")
        self.entry_correo = tk.Entry(self)
        self.entry_correo.grid(row=0, column=1)

        self.label_contrasena = tk.Label(self, text="Contraseña:")
        self.label_contrasena.grid(row=1, column=0, sticky="e")
        self.entry_contrasena = tk.Entry(self, show="*")
        self.entry_contrasena.grid(row=1, column=1)

        self.button_login = tk.Button(self, text="Login", command=self.validar_datos)
        self.button_login.grid(row=2, columnspan=2)

    def validar_datos(self):
        correo = self.entry_correo.get()
        contrasena = self.entry_contrasena.get()

        if correo == "" or contrasena == "":
            messagebox.showerror("Error", "Por favor ingrese correo y contraseña")
        elif correo == "andy@gmail.com" and contrasena == "12345":
            self.mostrar_mensaje_bienvenida()
        else:
            self.mostrar_error()

    def mostrar_mensaje_bienvenida(self):
        messagebox.showinfo("Bienvenido", "¡Login exitoso!")

    def mostrar_error(self):
        messagebox.showerror("Error", "Correo o contraseña incorrectos")

def main():
    login = Login()
    login.mainloop()

    main()
