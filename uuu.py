import tkinter as tk
from tkinter import messagebox
import calendar
from PIL import Image
from tkinter import *


# Variables globales
actividades = []
entry_nombre = None
entry_correo = None
entry_mes = None
entry_año = None
entry_actividad = None
entry_hora = None
text_calendario = None
text_cronograma = None
fuente = ("Calibri", 15)

ventana_tamano = "600x400"

def validar_correo(correo):
    """Valida si un correo electrónico es válido."""
    return "@" in correo and "." in correo

def ventana_bienvenida():
    """Crea la ventana de bienvenida con el mensaje inicial."""
    bienvenida_window = tk.Toplevel()
    bienvenida_window.title("Bienvenida")
    bienvenida_window.geometry(ventana_tamano)
    bienvenida_window.config(bg="lightblue")
    tk.Label(bienvenida_window, text="¡Bienvenido al Calendario Moment Time!", font=fuente, bg="lightblue").pack(pady=30)
    



    tk.Button(bienvenida_window, text="Aceptar para iniciar", font=fuente, command=lambda: [bienvenida_window.destroy(), ventana_nombre_correo()]).pack(pady=10)
    imagen=tk.PhotoImage(file="C:/Users/Natanael/Desktop/Programación/Python/Códigos/logo.png")
    etiqueta = tk.Label(bienvenida_window, image=imagen)
    etiqueta.pack()
    bienvenida_window.mainloop()
    


def ventana_nombre_correo():
    """Ventana para ingresar nombre y correo del usuario."""
    nombre_correo_window = tk.Toplevel()
    nombre_correo_window.title("Ingresar Nombre y Correo")
    nombre_correo_window.geometry(ventana_tamano)
    nombre_correo_window.config(bg="lightblue")
    
    tk.Label(nombre_correo_window, text="Ingrese su nombre:", font=fuente, bg="lightblue").pack(pady=5)
    global entry_nombre, entry_correo
    entry_nombre = tk.Entry(nombre_correo_window, font=fuente)
    entry_nombre.pack(pady=5)
    
    tk.Label(nombre_correo_window, text="Ingrese su correo:", font=fuente, bg="lightblue").pack(pady=5)
    entry_correo = tk.Entry(nombre_correo_window, font=fuente)
    entry_correo.pack(pady=5)
    
    def iniciar_con_datos():
        """Verifica que el nombre y correo sean válidos y procede."""
        nombre = entry_nombre.get().strip()
        correo = entry_correo.get().strip()
        if not nombre:
            messagebox.showerror("Error", "El nombre no puede estar vacío.")
        elif not validar_correo(correo):
            messagebox.showerror("Error", "Correo electrónico no válido.")
        else:
            messagebox.showinfo("Bienvenido", f"Hola {nombre}, ¡Bienvenido al Calendario Moment Time!")
            nombre_correo_window.destroy()
            ventana_menu()

    tk.Button(nombre_correo_window, text="Iniciar", font=fuente, command=iniciar_con_datos).pack(pady=10)

def ventana_menu():
    """Ventana del menú principal donde se eligen las opciones."""
    global entry_mes, entry_año, entry_actividad, entry_hora, text_calendario, text_cronograma
    menu_window = tk.Toplevel(root)
    menu_window.title("Opciones")
    menu_window.geometry(ventana_tamano)
    menu_window.config(bg="lightblue")

    tk.Label(menu_window, text="Seleccione una opción:", font=fuente, bg="lightblue").pack(pady=10)

    tk.Label(menu_window, text="Mes:", font=fuente, bg="lightblue").pack()
    entry_mes = tk.Entry(menu_window, font=fuente)
    entry_mes.pack()

    tk.Label(menu_window, text="Año:", font=fuente, bg="lightblue").pack()
    entry_año = tk.Entry(menu_window, font=fuente)
    entry_año.pack()

    tk.Button(menu_window, text="Ver Calendario", font=fuente, command=mostrar_calendario).pack(pady=5)

    text_calendario = tk.Text(menu_window, height=10, width=30, font=fuente)
    text_calendario.pack(pady=10)

    tk.Label(menu_window, text="Agregar actividad:", font=fuente, bg="lightblue").pack(pady=5)
    entry_actividad = tk.Entry(menu_window, font=fuente)
    entry_actividad.pack(pady=5)

    tk.Label(menu_window, text="Hora de la actividad:", font=fuente, bg="lightblue").pack(pady=5)
    entry_hora = tk.Entry(menu_window, font=fuente)
    entry_hora.pack(pady=5)

    tk.Button(menu_window, text="Agregar Actividad", font=fuente, command=agregar_actividad).pack(pady=5)

    tk.Button(menu_window, text="Ver Cronograma", font=fuente, command=mostrar_cronograma).pack(pady=5)

    text_cronograma = tk.Text(menu_window, height=10, width=30, font=fuente)
    text_cronograma.pack(pady=10)

    tk.Button(menu_window, text="Salir", font=fuente, command=salir).pack(pady=10)

def mostrar_calendario():
    """Muestra el calendario del mes y año especificados."""
    try:
        mes = int(entry_mes.get())
        año = int(entry_año.get())
        cal = calendar.month(año, mes)
        text_calendario.delete(1.0, tk.END)
        text_calendario.insert(tk.END, cal)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un mes y un año válidos.")

def agregar_actividad():
    """Agrega una actividad al cronograma."""
    actividad = entry_actividad.get().strip()
    hora = entry_hora.get().strip()
    if actividad and hora:
        actividades.append(f"{hora}: {actividad}")
        entry_actividad.delete(0, tk.END)
        entry_hora.delete(0, tk.END)
        mostrar_cronograma()
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una actividad y una hora.")

def mostrar_cronograma():
    """Muestra las actividades pendientes en el cronograma."""
    text_cronograma.delete(1.0, tk.END)
    if actividades:
        for actividad in actividades:
            text_cronograma.insert(tk.END, actividad + "\n")
    else:
        text_cronograma.insert(tk.END, "No hay actividades pendientes.")

def salir():
    """Cierra la aplicación."""
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal (solo se verá la ventana de bienvenida)

# Mostrar la ventana de bienvenida al inicio
ventana_bienvenida()

# Ejecutar la aplicación
root.mainloop()
