import tkinter as tk
from tkinter import *
from tkinter import messagebox
ventana=tk.Tk()
ventana.title("PetsCare")
ventana.geometry("1280x720")
ventana.config(bg="#D2DFE5")
ventana.iconbitmap("Patitas.ico")

imagen=tk.PhotoImage(file="PetsCare.png")
imagen=imagen.subsample(3,3)
foto=tk.Label(ventana, image=imagen,bg="#D2DFE5")
foto.pack()

mascota=None

def ABRIR_VENTANA2():
    global ventana2

    ventana2=tk.Toplevel()
    ventana2.title("PetsCare")
    ventana2.geometry("1280x720")
    ventana2.config(bg="#D2DFE5")
    ventana2.iconbitmap("Patitas.ico")

    imagen=tk.PhotoImage(file="PetsCare.png")
    imagen=imagen.subsample(6,6)
    foto=tk.Label(ventana2, image=imagen,bg="#D2DFE5")
    foto.image=imagen
    foto.place(relx=1.0, rely=0.0, anchor="ne")

    tk.Button(ventana2, text="REGISTRAR", font=("Arial",13,"bold"),bg="#A9C1CC",command=REGISTRO).pack()
    tk.Button(ventana2, text="REGRESAR AL MENÚ", font=("Arial",13,"bold"),bg="#A9C1CC",command=ventana2.destroy).pack()

def ABRIR_VENTANA3():
    global ventana3

    ventana3=tk.Toplevel()
    ventana3.title("PetsCare")
    ventana3.geometry("1280x720")
    ventana3.config(bg="#D2DFE5")
    ventana3.iconbitmap("Patitas.ico")

    imagen=tk.PhotoImage(file="PetsCare.png")
    imagen=imagen.subsample(6,6)
    foto=tk.Label(ventana3, image=imagen,bg="#D2DFE5")
    foto.image=imagen
    foto.place(relx=1.0, rely=0.0, anchor="ne")

    tk.Label(ventana3, text=" ",bg="#D2DFE5").pack(pady=100)
    tk.Button(ventana3, text="CALCULAR IMC", font=("Arial",13,"bold"),bg="#A9C1CC",command=IMC).pack()
    tk.Button(ventana3, text="REGRESAR AL MENÚ", font=("Arial",13,"bold"),bg="#A9C1CC",command=ventana3.destroy).pack()

class MASCOTA:
    def __init__(self,nombre,especie,raza,edad,peso,sexo,altura):
        self.nombre=nombre
        self.especie=especie
        self.raza=raza
        self.edad=edad
        self.peso=peso
        self.sexo=sexo
        self.altura=altura

def DATOS():
    global mascota

    nombre=entry_nombre.get()
    especie=entry_especie.get()
    raza=entry_raza.get()
    sexo=entry_sexo.get()
    edad=entry_edad.get()
    peso=entry_peso.get()
    altura=entry_altura.get()

    mascota=MASCOTA(nombre,especie,raza,edad,peso,sexo,altura)
    tk.Label(ventana2, text="Datos guardados")

def REGISTRO():

    global entry_nombre,entry_edad,entry_peso,entry_especie,entry_sexo,entry_raza,entry_altura

    tk.Label(ventana2, text="Ingrese los datos de su mascota:",font=("Arial",13),bg="#D2DFE5").pack()
    tk.Label(ventana2, text="Nombre:",font=("Arial",13),bg="#D2DFE5").pack()
    entry_nombre=tk.Entry(ventana2)
    entry_nombre.pack()
    tk.Label(ventana2, text="Edad(años):",font=("Arial",13),bg="#D2DFE5").pack()
    entry_edad=tk.Entry(ventana2)
    entry_edad.pack()
    tk.Label(ventana2, text="Peso(kg):",font=("Arial",13),bg="#D2DFE5").pack()
    entry_peso=tk.Entry(ventana2)
    entry_peso.pack()
    tk.Label(ventana2, text="Especie(perro/gato):",font=("Arial",13),bg="#D2DFE5").pack()
    entry_especie=tk.Entry(ventana2)
    entry_especie.pack()
    tk.Label(ventana2, text="Sexo(masculino/femenino):",font=("Arial",13),bg="#D2DFE5").pack()
    entry_sexo=tk.Entry(ventana2)
    entry_sexo.pack()
    tk.Label(ventana2, text="Raza(pequeña/mediana/grande):",font=("Arial",13),bg="#D2DFE5").pack()
    entry_raza=tk.Entry(ventana2)
    entry_raza.pack()
    tk.Label(ventana2, text="Ingresa altura hasta los hombros(cm):",font=("Arial",13),bg="#D2DFE5").pack()
    tk.Button(ventana2, text="¿Cómo puedo medir la altura hasta los hombros?",font=("Arial",11,"bold"),bg="#A9C1CC",command=A_HOMBROS).pack()
    entry_altura=tk.Entry(ventana2)
    entry_altura.pack()
    tk.Button(ventana2, text="Guardar datos",font=("Arial",13,"bold"),bg="#A9C1CC",command=DATOS).pack()

def A_HOMBROS():
    global imagen_perro,foto,informacion,b_ocultar

    imagen_perro=tk.PhotoImage(file="MEDIR.png")
    imagen_perro=imagen_perro.subsample(7,7)
    foto=tk.Label(ventana2, image=imagen_perro,bg="#D2DFE5")
    foto.pack()
    informacion=tk.Label(ventana2, text="Mide desde el suelo hasta la parte superior de la cruz\n(el punto más alto de los omóplatos).",font=("Arial",12),bg="#D2DFE5")
    informacion.pack()
    b_ocultar=tk.Button(ventana2, text="Ocultar", font=("Arial",11,"bold"),bg="#A9C1CC",command=ocultar)
    b_ocultar.pack()

def ocultar():
    foto.pack_forget()
    informacion.pack_forget()
    b_ocultar.pack_forget()

def IMC():
    global mascota

    if mascota is None:
        messagebox.showerror("ERROR","Primero registra una mascota")
        ventana3.destroy()
        return

    peso=float(mascota.peso)
    altura=float(mascota.altura)
    especie=mascota.especie
    altura=altura/100
    peso=peso*2.2046
    raza=mascota.raza
    IMC=peso/(altura**2)
    tk.Label(ventana3,text="El IMC de tu mascota es:",font=("Arial",14),bg="#D2DFE5").pack()
    tk.Label(ventana3, text=IMC).pack()
    if especie.lower() == "perro":
        if raza.lower() == "pequeña":
            peso_max=11
            peso_min=0
            if IMC<=peso_max and IMC>=peso_min:
                tk.Label(ventana3, text="Peso saludable",font=("Arial",14),bg="#D2DFE5").pack()
            elif IMC>peso_max:
                tk.Label(ventana3, text="Peso alto",font=("Arial",14),bg="#D2DFE5").pack()
            elif IMC<peso_min:
                tk.Label(ventana3, text="Peso bajo",font=("Arial",14),bg="#D2DFE5").pack()

        if raza.lower() == "mediana":
            peso_max=26
            peso_min=10
            if IMC<=peso_max and IMC>=peso_min:
                tk.Label(ventana3, text="Peso saludable",font=("Arial",14),bg="#D2DFE5").pack()
            elif IMC>peso_max:
                tk.Label(ventana3, text="Peso alto",font=("Arial",14),bg="#D2DFE5").pack()
            elif IMC<peso_min:
                tk.Label(ventana3, text="Peso bajo",font=("Arial",14),bg="#D2DFE5").pack()

        if raza.lower() == "grande":
            peso_max=46
            peso_min=25
            if IMC<=peso_max and IMC>=peso_min:
                tk.Label(ventana3, text="Peso saludable",font=("Arial",14),bg="#D2DFE5").pack()
            elif IMC>peso_max:
                tk.Label(ventana3, text="Peso alto",font=("Arial",14),bg="#D2DFE5").pack()
            elif IMC<peso_min:
                tk.Label(ventana3, text="Peso bajo",font=("Arial",14),bg="#D2DFE5").pack()

    if especie.lower() == "gato":
        if raza.lower() == "pequeña":
            peso_max=5
            peso_min=1
            if IMC<=peso_max and IMC>=peso_min:
                tk.Label(ventana3, text="Peso saludable",font=("Arial",14),bg="#D2DFE5").pack()
            elif IMC>peso_max:
                tk.Label(ventana3, text="Peso alto",font=("Arial",14),bg="#D2DFE5").pack()
            elif IMC<peso_min:
                tk.Label(ventana3, text="Peso bajo",font=("Arial",14),bg="#D2DFE5").pack()

        if raza.lower() == "mediana":
            peso_max=7
            peso_min=3
            if IMC<=peso_max and IMC>=peso_min:
                tk.Label(ventana3, text="Peso saludable",font=("Arial",14),bg="#D2DFE5").pack()
            elif IMC>peso_max:
                tk.Label(ventana3, text="Peso alto",font=("Arial",14),bg="#D2DFE5").pack()
            elif IMC<peso_min:
                tk.Label(ventana3, text="Peso bajo",font=("Arial",14),bg="#D2DFE5").pack()

        if raza.lower() == "grande":
            peso_max=10
            peso_min=5
            if IMC<=peso_max and IMC>=peso_min:
                tk.Label(ventana3, text="Peso saludable",font=("Arial",14),bg="#D2DFE5").pack()
            elif IMC>peso_max:
                tk.Label(ventana3, text="Peso alto",font=("Arial",14),bg="#D2DFE5").pack()
            elif IMC<peso_min:
                tk.Label(ventana3, text="Peso bajo",font=("Arial",14),bg="#D2DFE5").pack()

tk.Label(ventana, text="====PETS CARE====",font=("Impact",30,"bold"),fg="#7B8AAD",bg="#D2DFE5").pack(pady=20)
tk.Button(ventana, text="1. Registra a tus mascotas", font=("Arial",15,"bold"),bg="#A9C1CC",command=ABRIR_VENTANA2).pack()
tk.Button(ventana, text="2. IMC de mi mascota", font=("Arial",15,"bold"),bg="#A9C1CC", command=ABRIR_VENTANA3).pack()
tk.Button(ventana, text="3. Salir", font=("Arial",15,"bold"),bg="#A9C1CC", command=ventana.destroy).pack()
ventana.mainloop()