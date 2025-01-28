import random
import string

# Diccionario para almacenar usuarios y contraseñas
usuarios = {}

def generar_contrasena(length=8):
    """Genera una contraseña aleatoria de longitud especificada."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(length))

def registrar_usuario():  
    #"""Función para registrar un nuevo usuario."""
    nombre = input("Introduce tu nombre: ")
    if nombre in usuarios:
        print("El nombre de usuario ya está registrado.")
    else:
        contrasena = generar_contrasena()
        usuarios[nombre] = contrasena
        print(f"Usuario registrado con éxito. Tu contraseña es: {contrasena}")

def iniciar_sesion():
    """Función para manejar el inicio de sesión."""
    nombre = input("Introduce tu nombre: ")
    contrasena = input("Introduce tu contraseña: ")

    if nombre in usuarios and usuarios[nombre] == contrasena:
        print("Inicio de sesión exitoso.")
        return nombre
    else:
        print("Nombre de usuario o contraseña incorrectos.")
        return None

def ingresar_notas(nombre):
    """Función para ingresar notas y calcular el promedio."""
    notas = []
    while True:
        nota = input("Introduce una nota (o 'fin' para terminar): ")
        if nota.lower() == 'fin':
            break
        try:
            nota_float = float(nota)
            if 0 <= nota_float <= 10:  # Suponiendo que las notas están entre 0 y 10
                notas.append(nota_float)
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

    if notas:
        promedio = sum(notas) / len(notas)
        print(f"Tu promedio es: {promedio:.2f}")
        if promedio >= 6:  # Suponiendo que el promedio mínimo para pasar es 6
            print("¡Felicidades! Has pasado el semestre.")
        else:
            print("Lo siento, no has pasado el semestre.")
    else:
        print("No se ingresaron notas.")

def main():
    """Función principal del programa."""
    while True:
        print("\n1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            nombre = iniciar_sesion()
            if nombre:
                ingresar_notas(nombre)
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

# Ejecutar el programa
main()