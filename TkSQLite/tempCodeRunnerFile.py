Label(pestana5, text="Eliminar usuario", fg="#9617C6", font=("Times New Roman", 18)).pack()

eliminar1 = tk.StringVar()
Label(pestana5, text="Nombre: ", fg="#1769F8").pack()
Entry(pestana5, textvariable=eliminar1).pack()

eliminar2 = tk.StringVar()
Label(pestana5, text="Correo: ", fg="#1769F8").pack()
Entry(pestana5, textvariable=eliminar2).pack()

Button(pestana5, text="Eliminar", command=eliminarUsuario).pack()
