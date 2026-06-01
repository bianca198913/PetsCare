import tkinter as tk
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
    def __init__(self,nombre,especie,raza,edad,peso,sexo):
        self.nombre=nombre
        self.especie=especie
        self.raza=raza
        self.edad=edad
        self.peso=peso
        self.sexo=sexo

def DATOS(self):
    global MASCOTA

    nombre=entry_nombre.get()
    especie=entry_especie.get()
    raza=entry_raza.get()
    sexo=entry_sexo.get()
    edad=entry_edad.get()
    peso=entry_peso.get()

    MASCOTA=MASCOTA(nombre,especie,raza,sexo,edad,peso)
    pass

def REGISTRO():
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

tk.Label(ventana, text="PETS CARE",font=("Impact",30,"bold"),bg="#7B8AAD").pack(pady=20)
tk.Button(ventana, text="Registra a tus mascotas", font=("Arial",10,"bold"),bg="#A9C1CC",command=REGISTRO).pack()

ventana.mainloop()