import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

usuarios = {}
peliculas = {
    "Tron Legacy": ["A1", "A2", "A3", "B1", "B2", "B3",],
    "Sonic 3": ["C1", "C2", "C3", "D1", "D2", "D3"],
    "Interestelar": ["E1", "E2", "E3", "F1", "F2", "F3"],
}
reservas = {pelicula: [] for pelicula in peliculas}  
asiento_a_reservar = None  

# Funciones
def registrar():
    username = entry_username.get()
    password = entry_password.get()
    if username in usuarios:
        messagebox.showerror("Error", "El usuario ya existe.")
    else:
        usuarios[username] = password
        messagebox.showinfo("Éxito", "Registro exitoso.")
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)

def iniciar_sesion():
    username = entry_username.get()
    password = entry_password.get()
    if username in usuarios and usuarios[username] == password:
        messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
        ventana_principal()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

def ventana_principal():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Cinenat", font=("Calibri", 24)).pack(pady=20)
    imagen_pil= Image.open("logocine.png")
    imagen_redi= imagen_pil.resize((200,200))
    imagen_tk= ImageTk.PhotoImage(imagen_redi)
    etiqueta=tk.Label(root, image=imagen_tk)
    etiqueta.pack(anchor='center')

    tk.Button(root, text="Ver Películas", command=ver_peliculas).pack(pady=10)
    tk.Button(root, text="Ver Asientos Reservados", command=ver_asientos_reservados).pack(pady=10)
    tk.Button(root, text="Cerrar Sesión", command=cerrar_sesion).pack(pady=10)
    root.mainloop()

def ver_peliculas():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Películas Disponibles", font=("Calibri", 20)).pack(pady=20)

    imagen_pil= Image.open("Sonic 3.png")
    imagen_redi= imagen_pil.resize((200,300))
    imagen_tk= ImageTk.PhotoImage(imagen_redi)
    etiqueta=tk.Label(root, image=imagen_tk)
    etiqueta.pack(anchor='center')

    imagen_pil2= Image.open("Tron 3.png")
    imagen_redi2= imagen_pil2.resize((200,300))
    imagen_tk2= ImageTk.PhotoImage(imagen_redi2)
    etiqueta2=tk.Label(root, image=imagen_tk2)
    etiqueta2.place(x=360, y=82)

    imagen_pil3= Image.open("Interestelar2.jpg")
    imagen_redi3= imagen_pil3.resize((200,300))
    imagen_tk3= ImageTk.PhotoImage(imagen_redi3)
    etiqueta3=tk.Label(root, image=imagen_tk3)
    etiqueta3.place(x=800, y=82)

    for pelicula in peliculas.keys():
        tk.Button(root, text=pelicula, command=lambda p=pelicula: ver_asientos(p)).pack(pady=5)
    tk.Button(root, text="Volver", command=ventana_principal).pack(pady=10)
    root.mainloop()


def ver_asientos(pelicula):
    global pelicula_seleccionada
    pelicula_seleccionada = pelicula

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text=f"Asientos Disponibles para {pelicula}", font=("Calibri", 20)).pack(pady=20)

    # Crear un marco para los asientos
    frame_asientos = tk.Frame(root)
    frame_asientos.pack(pady=10)

    # Crear botones para los asientos
    asientos = peliculas[pelicula]
    for asiento in asientos:
        # Determinar el color del botón según si está reservado o no
        color = "red" if asiento in reservas[pelicula] else "green"
        btn = tk.Button(frame_asientos, text=asiento, bg=color, command=lambda a=asiento: seleccionar_asiento(a))
        btn.grid(row=0, column=asientos.index(asiento), padx=5, pady=5)

    tk.Button(root, text="Volver", command=ventana_principal).pack(pady=10)

def seleccionar_asiento(asiento):
    global asiento_a_reservar
    asiento_a_reservar = asiento  # Guardar el asiento seleccionado
    metodo_pago()  # Ir directamente a la pantalla de pago

def metodo_pago():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Métodos de Pago", font=("Calibri", 20)).pack(pady=20)
    tk.Button(root, text="Tarjeta de Crédito", command=pago_exitoso).pack(pady=5)
    tk.Button(root, text="PayPal", command=pago_exitoso).pack(pady=5)
    tk.Button(root, text="Efectivo", command=pago_exitoso).pack(pady=5)

    tk.Button(root, text="Volver", command=ventana_principal).pack(pady=10)

def pago_exitoso():
    global asiento_a_reservar
    if asiento_a_reservar:  
        reservas[pelicula_seleccionada].append(asiento_a_reservar) 
        for widget in root.winfo_children():
            if isinstance(widget, tk.Frame):
                for btn in widget.winfo_children():
                    if btn.cget("text") == asiento_a_reservar:
                        btn.config(bg="red")
        messagebox.showinfo("Reserva", f"Asiento {asiento_a_reservar} reservado para {pelicula_seleccionada}.")
        asiento_a_reservar = None 
    messagebox.showinfo("Pago", "Pago realizado con éxito.")
    ventana_principal()

def ver_asientos_reservados():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Asientos Reservados", font=("Calibri", 20)).pack(pady=20)

    imagen_pil= Image.open("Asientos.png")
    imagen_redi= imagen_pil.resize((200,200))
    imagen_tk= ImageTk.PhotoImage(imagen_redi)
    etiqueta=tk.Label(root, image=imagen_tk)
    etiqueta.pack(anchor='center')

    for pelicula in peliculas.keys():
        asientos_reservados = reservas[pelicula]
        if asientos_reservados:
            tk.Label(root, text=f"{pelicula}: {', '.join(asientos_reservados)}").pack(pady=5)
        else:
            tk.Label(root, text=f"{pelicula}: No hay asientos reservados.").pack(pady=5)

    tk.Button(root, text="Volver", command=ventana_principal).pack(pady=10)
    root.mainloop()

def cerrar_sesion():
    for widget in root.winfo_children():
        widget.destroy()
    crear_login()

def crear_login():

    tk.Label(root, text="BIENVENIDO A CINENAT", font=("Calibri", 24)).pack(pady=20)

    imagen_pil= Image.open("logocine.png")
    imagen_redi= imagen_pil.resize((200,200))
    imagen_tk= ImageTk.PhotoImage(imagen_redi)
    etiqueta=tk.Label(root, image=imagen_tk)
    etiqueta.pack(anchor='center')

    imagen_pil2= Image.open("logomio.png")
    imagen_redi2= imagen_pil2.resize((100,100))
    imagen_tk2= ImageTk.PhotoImage(imagen_redi2)
    etiqueta2=tk.Label(root, image=imagen_tk2)
    etiqueta2.place(x=0, y=0)


    tk.Label(root, text="Inicia sesión", font=("Calibri", 17)).pack(pady=5)

    global entry_username, entry_password
    entry_username = tk.Entry(root)
    entry_password = tk.Entry(root, show="*")

    tk.Label(root, text="Usuario").pack(pady=5)
    entry_username.pack(pady=5)
    tk.Label(root, text="Contraseña").pack(pady=5)
    entry_password.pack(pady=5)

    tk.Button(root, text="Iniciar Sesión", command=iniciar_sesion).pack(pady=5)
    tk.Button(root, text="Registrarse", command=registrar).pack(pady=5)
    tk.Label(root, text="No estás registrado? Introduce tus datos y pulsa en registrarse", font=("Calibri", 11)).pack(pady=20)
    root.mainloop()

# Crear la ventana principal
root = tk.Tk()
root.title("Cinenat")
root.minsize(1366,768)
root.maxsize(1366,768)
root.configure(bg="ghost whie")
root.attributes("-alpha",0.95)


# Iniciar la interfaz con el login
crear_login()

# Ejecutar el bucle principal
root.mainloop()