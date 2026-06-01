import tkinter as tk
from tkinter import *
ventana=tk.Tk()
ventana.title("PetsCare")
ventana.geometry("950x550")
ventana.config(bg="#D2DFE5")
ventana.iconbitmap("PetsCare.ico")

imagen=tk.PhotoImage(file="PetsCare.png")
imagen=imagen.subsample(7,7)
foto=tk.Label(ventana, image=imagen)
foto.place(relx=1.0, rely=0.0, anchor="ne")

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

def REGISTRO():

    global entry_nombre,entry_edad,entry_peso,entry_especie,entry_sexo,entry_raza,entry_altura

    tk.Label(ventana, text="Ingrese los datos de su mascota: \nNombre:").pack()
    entry_nombre=tk.Entry(ventana)
    entry_nombre.pack()
    tk.Label(ventana, text="Edad:").pack()
    entry_edad=tk.Entry(ventana)
    entry_edad.pack()
    tk.Label(ventana, text="Peso:").pack()
    entry_peso=tk.Entry(ventana)
    entry_peso.pack()
    tk.Label(ventana, text="Especie(perro/gato):").pack()
    entry_especie=tk.Entry(ventana)
    entry_especie.pack()
    tk.Label(ventana, text="Sexo(masculino/femenino):").pack()
    entry_sexo=tk.Entry(ventana)
    entry_sexo.pack()
    tk.Label(ventana, text="Raza(pequeo/mediano/grande):").pack()
    entry_raza=tk.Entry(ventana)
    entry_raza.pack()
    tk.Label(ventana, text="Ingresa la altura:").pack()
    entry_altura=tk.Entry(ventana)
    entry_altura.pack()
    tk.Button(ventana, text="Guardar datos",command=DATOS).pack()

def BCS():
    peso=float(mascota.peso)
    altura=float(mascota.altura)
    especie=mascota.especie
    raza=mascota.raza
    BCS=peso/(altura**2)
    tk.Label(ventana,text="El BCS de tu mascota es:").pack()
    tk.Label(ventana, text=BCS).pack()
    if especie.lower() == "perro":
        if raza.lower() == "pequeña":
            peso_max=11
            peso_min=0
            if BCS<=peso_max and BCS>=peso_min:
                tk.Label(ventana, text="Peso saludable").pack()
            elif BCS>peso_max:
                tk.Label(ventana, text="Peso alto").pack()
            elif BCS<peso_min:
                tk.Label(ventana, text="Peso bajo").pack()

        if raza.lower() == "mediana":
            peso_max=26
            peso_min=10
            if BCS<=peso_max and BCS>=peso_min:
                tk.Label(ventana, text="Peso saludable").pack()
            elif BCS>peso_max:
                tk.Label(ventana, text="Peso alto").pack()
            elif BCS<peso_min:
                tk.Label(ventana, text="Peso bajo").pack()

        if raza.lower() == "grande":
            peso_max=46
            peso_min=25
            if BCS<=peso_max and BCS>=peso_min:
                tk.Label(ventana, text="Peso saludable").pack()
            elif BCS>peso_max:
                tk.Label(ventana, text="Peso alto").pack()
            elif BCS<peso_min:
                tk.Label(ventana, text="Peso bajo").pack()

    if especie.lower() == "gato":
        if raza.lower() == "pequeña":
            peso_max=5
            peso_min=1
            if BCS<=peso_max and BCS>=peso_min:
                tk.Label(ventana, text="Peso saludable").pack()
            elif BCS>peso_max:
                tk.Label(ventana, text="Peso alto").pack()
            elif BCS<peso_min:
                tk.Label(ventana, text="Peso bajo").pack()

        if raza.lower() == "mediana":
            peso_max=7
            peso_min=3
            if BCS<=peso_max and BCS>=peso_min:
                tk.Label(ventana, text="Peso saludable").pack()
            elif BCS>peso_max:
                tk.Label(ventana, text="Peso alto").pack()
            elif BCS<peso_min:
                tk.Label(ventana, text="Peso bajo").pack()

        if raza.lower() == "grande":
            peso_max=10
            peso_min=5
            if BCS<=peso_max and BCS>=peso_min:
                tk.Label(ventana, text="Peso saludable").pack()
            elif BCS>peso_max:
                tk.Label(ventana, text="Peso alto").pack()
            elif BCS<peso_min:
                tk.Label(ventana, text="Peso bajo").pack()

tk.Label(ventana, text="PETS CARE",font=("Impact",30,"bold"),bg="#7B8AAD").pack(pady=20)
tk.Button(ventana, text="Registra a tus mascotas", font=("Arial",10,"bold"),bg="#A9C1CC",command=REGISTRO).pack()
tk.Button(ventana, text="1. BCS de mi mascota", font=("Arial",10,"bold"),bg="#A9C1CC", command=BCS).pack()
ventana.mainloop()