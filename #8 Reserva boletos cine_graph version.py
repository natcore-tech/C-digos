import tkinter as tk
from tkinter import messagebox

def iniciar_sesion():
    messagebox.showinfo("Iniciar sesión", "Función de iniciar sesión no implementada aún.")

def crear_cuenta():
    messagebox.showinfo("Crear cuenta", "Función de crear cuenta no implementada aún.")

def peliculas_disponibles():
    messagebox.showinfo("Películas disponibles", "Lista de películas no implementada aún.")

def salir():
    if messagebox.askyesno("Salir", "¿Estás seguro de que deseas salir?"):
        root.destroy()

# Crear ventana principal
root = tk.Tk()
root.title("Cinenat - Reserva de boletos de cine")
root.geometry("400x300")

# Bienvenida
label_bienvenida = tk.Label(root, text="Bienvenido a Cinenat", font=("Helvetica", 16, "bold"))
label_bienvenida.pack(pady=10)

label_subtitulo = tk.Label(root, text="Por favor inicia sesión o crea tu cuenta para darte un mejor servicio")
label_subtitulo.pack(pady=5)

# Botones
btn_iniciar_sesion = tk.Button(root, text="Iniciar sesión", font=("Helvetica", 12), command=iniciar_sesion)
btn_iniciar_sesion.pack(pady=5, fill=tk.X, padx=50)

btn_crear_cuenta = tk.Button(root, text="Crear cuenta", font=("Helvetica", 12), command=crear_cuenta)
btn_crear_cuenta.pack(pady=5, fill=tk.X, padx=50)

btn_peliculas_disponibles = tk.Button(root, text="Películas disponibles", font=("Helvetica", 12), command=peliculas_disponibles)
btn_peliculas_disponibles.pack(pady=5, fill=tk.X, padx=50)

btn_salir = tk.Button(root, text="Salir", font=("Helvetica", 12), command=salir)
btn_salir.pack(pady=5, fill=tk.X, padx=50)

root.mainloop()
