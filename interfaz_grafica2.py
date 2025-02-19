import tkinter as tk
from PIL import Image, ImageTk

ventana= tk.Tk()
ventana.geometry("720x480")

tk.Label(ventana, text="Cinenat", font=("Arial", 24)).pack(pady=20)
imagen_pil= Image.open("Sonic 3.png")
imagen_redi= imagen_pil.resize((200,300))
imagen_tk= ImageTk.PhotoImage(imagen_redi)
etiqueta=tk.Label(ventana, image=imagen_tk)
etiqueta.pack(anchor='center')

imagen_pil2= Image.open("Tron 3.png")
imagen_redi2= imagen_pil2.resize((200,300))
imagen_tk2= ImageTk.PhotoImage(imagen_redi2)
etiqueta2=tk.Label(ventana, image=imagen_tk2)
etiqueta2.place(x=360, y=82)


imagen_pil3= Image.open("Tron 3.png")
imagen_redi3= imagen_pil3.resize((200,300))
imagen_tk3= ImageTk.PhotoImage(imagen_redi3)
etiqueta3=tk.Label(ventana, image=imagen_tk3)
etiqueta3.place(x=800, y=82)


ventana.mainloop()
