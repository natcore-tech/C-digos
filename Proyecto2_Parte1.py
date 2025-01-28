import random
import string
import Proyecto2_Parte2

# Diccionario para almacenar usuarios y contraseñas
usuarios = {}

def gen(length=8):
    # """Genera una contraseña aleatoria de longitud especificada."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(length))

def reg():  
    #"""Función para registrar un nuevo usuario."""
    nombre = input("Introduce tu nombre: ")
    if nombre in usuarios:
        print("El nombre de usuario ya está registrado.")
    else:
        contrasena = gen()
        usuarios[nombre] = contrasena
        print(f"Usuario registrado con éxito. Tu contraseña es: {contrasena}")

def log():
    """Función para manejar el inicio de sesión."""
    nombre = input("Introduce tu nombre: ")
    contrasena = input("Introduce tu contraseña: ")

    if nombre in usuarios and usuarios[nombre] == contrasena:
        print("\nInicio de sesión exitoso.")
        return nombre
    else:
        print("\nNombre de usuario o contraseña incorrectos.")
        return None
        
def Login_PromedioYCertificado():
    print("")
    print("           ¡Bienvenidos al programa de registro y certificación!")
    print("\nEste espacio está diseñado para ayudarte a obtener tu certificado calculando \ntu promedio de notas de forma sencilla y rápida.")
    print("Solo necesitas registrarte y proporcionar tus calificaciones \nY nosotros nos encargamos de generar tu promedio.")
    print("\n                                ¡Comencemos!")
    while True:
        print("-------------------------------------------------------------------------------")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        print("-------------------------------------------------------------------------------")
        opcion = input("Elige una opción: ")
        print("-------------------------------------------------------------------------------")
        if opcion == '1':
            reg()
        elif opcion == '2':
            nombre = log()
            if nombre:
                Proyecto2_Parte2.Promedio_Certificado()
        elif opcion == '3':
            print("Saliendo del programa..... \n")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

Login_PromedioYCertificado()
