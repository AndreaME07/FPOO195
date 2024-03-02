from tkinter import Tk, Frame
#llamamos la librería o importamos la librería frame

#1. Creamos la ventana
Ventana= Tk() #Uso de POO creando un Obj Ventana
Ventana.title("Ejemplo con 3 Frames")
Ventana.geometry("600x400")

#2. Colocamos las secciones o los frames de la ventana
seccion1=Frame(Ventana, bg="pink")
seccion1.pack(expand=True, fill='both')

seccion2=Frame(Ventana, bg="blue")
seccion2.pack(expand=True, fill='both')

seccion3=Frame(Ventana, bg="purple")
seccion3.pack(expand=True, fill='both')




#Ejecuta la ventana aquí se usa un método
Ventana.mainloop()