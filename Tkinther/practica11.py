from tkinter import Tk, Frame, Button, messagebox
#llamamos la librería o importamos la librería frame

#metodos para mensaje
def mostrarMensajes():
    print(messagebox.showinfo('showinfo', 'Information'))
    print(messagebox.showerror('showerror', 'Error'))
    print(messagebox.showwarning('showwarning', 'Warning'))
    print(messagebox.askquestion(message="¿Deseas continuar?", title="Soy el título"))

# 

def addbtn():
    botonVerde.config(text="+")
    botonRosa= Button(seccion3,text="Nuevo", bg="#FF01DC")
    botonRosa.configure(height=2,width=10)
    botonRosa.pack()

#1. Creamos la ventana
Ventana= Tk() #Uso de POO creando un Obj Ventana
Ventana.title("Ejemplo con 3 Frames")
Ventana.geometry("600x400")

#2. Colocamos las secciones o los frames de la ventana
seccion1=Frame(Ventana, bg="#BA2DCB")
seccion1.pack(expand=True, fill='both')
#expand agarra todo lo que tenga disponible el frame
# fill rellena todo lo que seleccionemos en el frame

seccion2=Frame(Ventana, bg="#9856A0")
seccion2.pack(expand=True, fill='both')

seccion3=Frame(Ventana, bg="#D07DDA")
seccion3.pack(expand=True, fill='both')


#3. Posicionar botones

#place
botonAzul= Button(seccion1,text="Azul", fg="#0B7A6E")
botonAzul.place(x=100,y=60, width=100, height=30)

#grid 
botonNegro= Button(seccion2,text="Negro", fg="#FFFFFF", bg="#090909")
botonNegro.configure(width=10, height=2)
botonNegro.grid(row=0,column=1)

botonAmarillo= Button(seccion2,text="amarillo", bg="#fbff00", command=mostrarMensajes)
botonAmarillo.configure(width=10, height=2)
botonAmarillo.grid(row=1,column=3)

#pack
botonVerde= Button(seccion3,text="Verde", bg="#06e813", command=addbtn)
botonVerde.configure(width=10, height=2)
botonVerde.pack()

botonVerde2= Button(seccion3,text="Verde2", bg="#06e813")
botonVerde2.configure(width=10, height=2)
botonVerde2.pack()
#Ejecuta la ventana aquí se usa un método
Ventana.mainloop()