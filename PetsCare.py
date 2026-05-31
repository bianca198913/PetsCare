import tkinter as tk
ventana=tk.Tk()
ventana.title("PetsCare")
ventana.geometry("950x350")
ventana.config(bg="#D2DFE5")
ventana.iconbitmap("PetsCare.ico")

imagen=tk.PhotoImage(file="PetsCare.png")
imagen=imagen.subsample(7,7)

class MASCOTA:
    def __init__ (self,especie,nombre,raza,sexo,edad,peso,est):
        self.especie=especie
        self.nombre=nombre
        self.raza=raza
        self.sexo=sexo
        self.edad=edad
        self.peso=peso
        self.est=est

    def EDAD_MASCOTA (self):
        if self.especie==entry_perro.get():
            match self.raza:
                case 1:
                    match self.edad:
                        case 1:
                            return self.nombre+" tiene 15 años humanos"
                        case 2:
                            return self.nombre+" tiene 24 años humanos"
                        case 3:
                            return self.nombre+" tiene 28 años humanos"
                        case 4:
                            return self.nombre+" tiene 32 años humanos"
                        case 5:
                            return self.nombre+" tiene 36 años humanos"
                        case 6:
                            return self.nombre+" tiene 40 años humanos"
                        case 7:
                            return self.nombre+" tiene 44 años humanos"
                        case 8:
                            return self.nombre+" tiene 48 años humanos"
                        case 9:
                            return self.nombre+" tiene 52 años humanos"
                        case 10:
                            return self.nombre+" tiene 56 años humanos"
                        case 11:
                            return self.nombre+" tiene 60 años humanos"
                        case 12:
                            return self.nombre+" tiene 64 años humanos"
                        case 13:
                            return self.nombre+" tiene 68 años humanos"
                        case 14:
                            return self.nombre+" tiene 72 años humanos"
                        case 15:
                            return self.nombre+" tiene 76 años humanos"
                case 2:
                    match self.edad:
                        case 1:
                            return self.nombre+" tiene 15 años humanos"
                        case 2:
                            return self.nombre+" tiene 24 años humanos"
                        case 3:
                            return self.nombre+" tiene 28 años humanos"
                        case 4:
                            return self.nombre+" tiene 32 años humanos"
                        case 5:
                            return self.nombre+" tiene 36 años humanos"
                        case 6:
                            return self.nombre+" tiene 40 años humanos"
                        case 7:
                            return self.nombre+" tiene 47 años humanos"
                        case 8:
                            return self.nombre+" tiene 51 años humanos"
                        case 9:
                            return self.nombre+" tiene 56 años humanos"
                        case 10:
                            return self.nombre+" tiene 60 años humanos"
                        case 11:
                            return self.nombre+" tiene 65 años humanos"
                        case 12:
                            return self.nombre+" tiene 69 años humanos"
                        case 13:
                            return self.nombre+" tiene 74 años humanos"
                        case 14:
                            return self.nombre+" tiene 78 años humanos"
                        case 15:
                            return self.nombre+" tiene 83 años humanos"
                case 3:
                    match self.edad:
                        case 1:
                            return self.nombre+" tiene 15 años humanos"
                        case 2:
                            return self.nombre+" tiene 24 años humanos"
                        case 3:
                            return self.nombre+" tiene 28 años humanos"
                        case 4:
                            return self.nombre+" tiene 32 años humanos"
                        case 5:
                            return self.nombre+" tiene 36 años humanos"
                        case 6:
                            return self.nombre+" tiene 46 años humanos"
                        case 7:
                            return self.nombre+" tiene 50 años humanos"
                        case 8:
                            return self.nombre+" tiene 55 años humanos"
                        case 9:
                            return self.nombre+" tiene 61 años humanos"
                        case 10:
                            return self.nombre+" tiene 66 años humanos"
                        case 11:
                            return self.nombre+" tiene 72 años humanos"
                        case 12:
                            return self.nombre+" tiene 77 años humanos"
                        case 13:
                            return self.nombre+" tiene 82 años humanos"
                        case 14:
                            return self.nombre+" tiene 88 años humanos"
                        case 15:
                            return self.nombre+" tiene 93 años humanos"

        else:
            match self.raza:
                case 1:
                    match self.edad:
                        case 1:
                            return self.nombre+" tiene 15 años humanos"
                        case 2:
                            return self.nombre+" tiene 24 años humanos"
                        case 3:
                            return self.nombre+" tiene 28 años humanos"
                        case 4:
                            return self.nombre+" tiene 32 años humanos"
                        case 5:
                            return self.nombre+" tiene 36 años humanos"
                        case 6:
                            return self.nombre+" tiene 40 años humanos"
                        case 7:
                            return self.nombre+" tiene 44 años humanos"
                        case 8:
                            return self.nombre+" tiene 48 años humanos"
                        case 9:
                            return self.nombre+" tiene 52 años humanos"
                        case 10:
                            return self.nombre+" tiene 56 años humanos"
                        case 11:
                            return self.nombre+" tiene 60 años humanos"
                        case 12:
                            return self.nombre+" tiene 64 años humanos"
                        case 13:
                            return self.nombre+" tiene 68 años humanos"
                        case 14:
                            return self.nombre+" tiene 72 años humanos"
                        case 15:
                            return self.nombre+" tiene 76 años humanos"
                        case 16:
                            return self.nombre+"tiene 80 años humanos"
                        case 17:
                            return self.nombre+"tiene 84 años humanos"
                        case 18:
                            return self.nombre+"tiene 88 años humanos"
                        case 19:
                            return self.nombre+"tiene 92 años humanos"
                        case 20:
                            return self.nombre+"tiene 96 años humanos"
                        case 21:
                            return self.nombre+"tiene 100 años humanos"

class DUEÑO:
    def __init__ (self, municipio):
        self.municipio=municipio

def EDAD_HUMANA():
    resultado.config(text=MASCOTA.EDAD_MASCOTA(self))

def DATOS(self):
    global MASCOTA

    nombre=entry_nombre.get()
    especie=entry_especie.get()
    raza=entry_raza.get()
    sexo=entry_sexo.get()
    edad=entry_edad.get()
    peso=entry_peso.get()
    est=entry_est.get()

    mascota=MASCOTA(nombre,especie,raza,sexo,edad,peso,est)

    resultado.config(text="DATOS REGISTRADOS.")

def MENU():
    return("1. Cuidados de mi mascota\n2. Edad humana de mi mascota\n3.IMC de mi mascota\n4.Clinicas veterinarias cerca de mi\n5.Salir")

foto=tk.Label(ventana, image=imagen)
foto.place(relx=1.0, rely=0.0, anchor="ne")
tk.Label(ventana, text="PETS CARE",font=("Impact",30,"bold"),bg="#7B8AAD").pack(pady=20)
tk.Label(ventana, text=MENU(),font=("Arial",12),bg="#A9C1CC").pack()
tk.Button(ventana, text="1. Cuidados de mi mascota", font=("Arial",10,"bold"),bg="#A9C1CC",command=DATOS).pack()
entry_nombre=tk.Entry(ventana,font=("Arial",10),bg="#B4BFD5")
entry_nombre.pack()
entry_especie=tk.Entry(ventana)
entry_especie.pack()
entry_raza=tk.Entry(ventana)
entry_raza.pack()
entry_sexo=tk.Entry(ventana)
entry_sexo.pack()
entry_edad=tk.Entry(ventana)
entry_edad.pack()
entry_peso=tk.Entry(ventana)
entry_peso.pack()
entry_est=tk.Entry(ventana)
entry_est.pack()
tk.Button(ventana, text="2. Edad humana", command=EDAD_HUMANA).pack()
tk.Button(ventana, text="3. IMC de mi mascota").pack()
tk.Button(ventana, text="4. Clinicas veterinarias cerca de mi").pack()
tk.Button(ventana, text="5. Salir").pack()

resultado=tk.Label(ventana,text="")
resultado.pack()
ventana.mainloop()